import os
import sys

from main.settings import BASE_DIR

DEBUG = True if os.environ.get('DEBUG', 'off') == 'on' else False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("DB_NAME"),
        'PASSWORD': os.environ.get("DB_PASSWORD"),
        'USER': os.environ.get("DB_USER"),
        'HOST': os.environ.get("DB_HOST"),
        'PORT': os.environ.get("DB_PORT")
    }
}

# Static assets
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [STATIC_DIR]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


