from .base import *
import os

ENV = os.getenv('.env', 'local')

if os.environ.get("ENV") == 'Production':
    from .production import *
elif os.environ.get("ENV") == 'local':
    from .local import *
else:
    from .local import *