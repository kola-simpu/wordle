from controllers import health, auth, games


def apply_routes(app):
    app.add_url_rule('/', view_func=health.index, methods=['GET'], strict_slashes=False)
    # Auth
    app.add_url_rule('/auth/login', view_func=auth.login, methods=['POST'], strict_slashes=False)
    # Games
    app.add_url_rule('/game/create', view_func=games.save, methods=['POST'], strict_slashes=False)
