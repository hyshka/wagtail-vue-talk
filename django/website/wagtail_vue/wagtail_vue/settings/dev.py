"""Development settings and globals."""
from .settings_base import *  # noqa

# ======== DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG  # noqa
# ======== END DEBUG CONFIGURATION


# ======== EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# ======== END EMAIL CONFIGURATION


# ======== DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/app/website/wagtail_vue/wagtail_vue/settings/database.sqlite3',
    }
}
# ======== END DATABASE CONFIGURATION


# ======== CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
# ======== END CACHE CONFIGURATION


# ======== TOOLBAR CONFIGURATION
# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation # noqa
INSTALLED_APPS += ( # noqa
    'debug_toolbar',
)

MIDDLEWARE += ( # noqa
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)


# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation # noqa
INTERNAL_IPS = ('127.0.0.1', '172.17.0.1', '172.17.0.2')

# ======== END TOOLBAR CONFIGURATION

ALLOWED_HOSTS += [ # noqa
    'localhost',
    'backend',
] + list(INTERNAL_IPS)

CORS_ORIGIN_ALLOW_ALL = True

try:
    from .local_dev import * # noqa
except ImportError:
    pass
