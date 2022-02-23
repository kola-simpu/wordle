from controllers import health, auth


def apply_routes(app):
    app.add_url_rule('/', view_func=health.index, methods=['GET'], strict_slashes=False)
    # Auth
    app.add_url_rule('/auth/login', view_func=auth.login, methods=['GET'], strict_slashes=False)
