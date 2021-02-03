from .base import *


import debug_toolbar

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7a=h!33%%s92lbky%wx=mo$(b7c1*enmgou=#s_o6tr3-jz2bd'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = INSTALLED_APPS+[
	'debug_toolbar'
]


MIDDLEWARE = MIDDLEWARE+[
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS=("127.0.0.1","172.17.0.1")


try:
    from .local import *
except ImportError:
    pass
