from connections.psql import PSQL


class Word:
    @staticmethod
    def create(word_obj):
        query = ' INSERT INTO words (word) ' \
                ' VALUES (%(word)s) ' \
                ' RETURNING id '
        conn = PSQL(query, word_obj)
        insert_id = conn.execute().fetchone()['id']
        conn.commit()
        return insert_id

    @staticmethod
    def update(word_obj):
        update_id = PSQL.update('words', word_obj)
        return update_id

    @staticmethod
    def delete(word_id):
        query_vars = {'id': word_id}
        query = ' DELETE FROM words WHERE id = %(id)s '
        conn = PSQL(query, query_vars)
        delete_id = conn.execute().fetchone()['id']
        conn.commit()
        return delete_id

    @staticmethod
    def get_all_approved():
        query = ' SELECT id, word FROM words '
        conn = PSQL(query)
        result = conn.execute().fetchall()
        conn.close()
        return result

    @staticmethod
    def get(word_id: int):
        query_vars = {'id': word_id}
        query = ' SELECT id, word FROM words WHERE id = %(id)s '
        conn = PSQL(query, query_vars)
        result = conn.execute().fetchone()
        conn.close()
        return result
