import os
import sys
from .. import settings
from .base import AUTH_PASSWORD_VALIDATORS

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = settings.DATABASES

AUTH_PASSWORD_VALIDATORS = AUTH_PASSWORD_VALIDATORS