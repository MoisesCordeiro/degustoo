from .settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'degustoo',
        'HOST': 'localhost',
        'USER': 'userdegustoo',
        'PASSWORD': 'passdegustoo',
        'PORT': '5432',
    }
}
