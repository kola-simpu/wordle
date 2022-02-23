from connections.psql import PSQL


class Game:
    @staticmethod
    def create(game_obj):
        query = ' INSERT INTO games (name, word) ' \
                ' VALUES (%(name)s,%(word_id)s) ' \
                ' RETURNING id '
        conn = PSQL(query, game_obj)
        insert_id = conn.execute().fetchone()['id']
        conn.commit()
        return insert_id
