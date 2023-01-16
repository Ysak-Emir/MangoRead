import os
import sys
from .base import INSTALLED_APPS
from main.settings import BASE_DIR
from .base import SECRET_KEY, MIDDLEWARE, TEMPLATES, AUTH_USER_MODEL, AUTH_PASSWORD_VALIDATORS
from .jazzmin import JAZZMIN_SETTINGS


SECRET_KEY = SECRET_KEY
INSTALLED_APPS = INSTALLED_APPS
MIDDLEWARE = MIDDLEWARE
TEMPLATES = TEMPLATES
AUTH_USER_MODEL = AUTH_USER_MODEL
AUTH_PASSWORD_VALIDATORS = AUTH_PASSWORD_VALIDATORS
JAZZMIN_SETTINGS = JAZZMIN_SETTINGS

DEBUG = True if os.environ.get('DEBUG', 'off') == 'on' else False
ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("DB_NAME", "manga_db"),
        'PASSWORD': os.environ.get("DB_PASSWORD", "123456"),
        'USER': os.environ.get("DB_USER", "admin"),
        'HOST': os.environ.get("DB_HOST", "db"),
        'PORT': '5432'
    }
}

# Static assets
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [STATIC_DIR]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


ROOT_URLCONF = 'main.urls'