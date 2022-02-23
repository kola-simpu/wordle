import json
import logging
import os

import psycopg2
from psycopg2.extras import RealDictCursor


class PSQL:
    def __init__(self, query=None, query_vars=None):
        self.query = query
        self.query_vars = query_vars
        self.conn = psycopg2.connect(host=os.getenv('DB_SERVER'), user=os.getenv('DB_USER'), password=os.getenv('DB_PASS'), database=os.getenv('DB_NAME'), port=os.getenv('DB_PORT'))

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
        uuid = column_obj.pop('uuid')
        query = ' UPDATE {} SET '.format(table_name)
        set_values = []
        for column, value in column_obj.items():
            column_obj[column] = json.dumps(value) if isinstance(value, dict) else value
            set_values.append('{} = %({})s'.format(column, column))
        query += ', '.join(set_values)
        query += ' WHERE uuid = %(uuid)s RETURNING uuid '
        column_obj.update({'uuid': uuid})
        conn = PSQL(query, column_obj)
        update_uuid = conn.execute().fetchone()['uuid']
        conn.commit()
        return update_uuid

    def commit(self):
        self.conn.commit()
        self.conn.cursor().close()
        self.conn.close()

    def close(self):
        self.conn.cursor().close()
        self.conn.close()
