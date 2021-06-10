from .routes import bp


def init_app(app):
    '''
    Init bgp module
    '''

    app.register_blueprint(bp)
