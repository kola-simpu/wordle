import json
import logging
from decouple import config as env

import psycopg2
from psycopg2.extras import RealDictCursor


class PSQL:
    def __init__(self, query=None, query_vars=None):
        self.query = query
        self.query_vars = query_vars
        self.conn = psycopg2.connect(host=env('DB_SERVER'), user=env('DB_USER'), password=env('DB_PASS'), database=env('DB_NAME'), port=env('DB_PORT'))

    def execute(self):
        try:
            cur = self.conn.cursor(cursor_factory=RealDictCursor)
            if self.query_vars:
                if isinstance(self.query_vars, dict):
                    cur.execute(self.query, self.query_vars)
                    logging.info(cur.query.decode('utf-8'))
                    logging.info(self.query_vars)
                else:
                    self.query_vars = tuple(self.query_vars)
                    query = cur.mogrify(self.query, self.query_vars)
                    cur.execute(query)
                    logging.info(cur.query.decode('utf-8'))
                    logging.info(self.query_vars)
            else:
                cur.execute(self.query)

            rows = cur

            return rows

        except psycopg2.IntegrityError as e:
            logging.error(e)
            raise e

    def insert_id(self):
        return self.conn.insert_id()

    @staticmethod
    def update(table_name: str, column_obj: dict) -> str:
        obj_id = column_obj.pop('id')
        query = ' UPDATE {} SET '.format(table_name)
        set_values = []
        for column, value in column_obj.items():
            column_obj[column] = json.dumps(value) if isinstance(value, dict) else value
            set_values.append('{} = %({})s'.format(column, column))
        query += ', '.join(set_values)
        query += ' WHERE id = %(id)s RETURNING id '
        column_obj.update({'id': obj_id})
        conn = PSQL(query, column_obj)
        update_uuid = conn.execute().fetchone()['id']
        conn.commit()
        return update_uuid

    def commit(self):
        self.conn.commit()
        self.conn.cursor().close()
        self.conn.close()

    def close(self):
        self.conn.cursor().close()
        self.conn.close()
