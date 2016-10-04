from dnsaas.settings.base import *  # noqa


def only_true(request):
    '''For django debug toolbar.'''
    return True

DEBUG = True

INSTALLED_APPS = INSTALLED_APPS + (  # noqa
    'debug_toolbar',
)

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (  # noqa
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': "%s.only_true" % __name__,
}
