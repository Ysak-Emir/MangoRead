import os
import sys

from main.settings import BASE_DIR

DEBUG = True if os.environ.get('DEBUG', 'off') == 'on' else False
ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("DB_NAME", "manga_db"),
        'PASSWORD': os.environ.get("DB_PASSWORD", "123456"),
        'USER': os.environ.get("DB_USER", "admin"),
        'HOST': os.environ.get("DB_HOST", "db"),
        'PORT': 5432
    }
}

# Static assets
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [STATIC_DIR]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


