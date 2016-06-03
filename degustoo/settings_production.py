#coding: utf-8
from .settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbdegustoo',
        'HOST': 'localhost', #or host database
        'USER': 'userdegustoo',
        'PASSWORD': 'degustoo2016',
    }
}

MEDIA_ROOT = '/home/webapps/degustoo/media'
STATIC_ROOT = '/home/webapps/degustoo/static_collected'