from controllers import health, auth, games, words


def apply_routes(app):
    app.add_url_rule('/', view_func=health.index, methods=['GET'], strict_slashes=False)
    # Auth
    app.add_url_rule('/auth/login', view_func=auth.login, methods=['POST'], strict_slashes=False)
    # Games
    app.add_url_rule('/game/create', view_func=games.save_game, methods=['POST'], strict_slashes=False)
    # Words
    app.add_url_rule('/word/create', view_func=words.save_word, methods=['POST'], strict_slashes=False)
    app.add_url_rule('/word/update', view_func=words.save_word, methods=['PATCH'], strict_slashes=False)
    app.add_url_rule('/word/delete', view_func=words.save_word, methods=['DELETE'], strict_slashes=False)
    app.add_url_rule('/words', view_func=words.get_approved, methods=['GET'], strict_slashes=False)
