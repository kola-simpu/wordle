from controllers import health


def apply_routes(app):
    app.add_url_rule('/', view_func=health.index, methods=['GET'], strict_slashes=False)
