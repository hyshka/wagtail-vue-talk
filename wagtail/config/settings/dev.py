"""Settings for development."""
from .base import *

ALLOWED_HOSTS = ["localhost"]

DEBUG = True
TEMPLATES[0]["OPTIONS"]["debug"] = DEBUG

try:
    from .local import *  # noqa
except ImportError:
    pass
