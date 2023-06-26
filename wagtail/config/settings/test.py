from .base import *  # noqa

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}

PASSWORD_HASHERS = ("django.contrib.auth.hashers.MD5PasswordHasher",)

DEBUG = False

try:
    from .local_test import *  # noqa
except ImportError:
    pass
