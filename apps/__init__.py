from . import bgp


def init(app):
    '''
    Init modules
    '''
    bgp.init_app(app)
