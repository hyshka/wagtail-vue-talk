# -*- coding: utf-8 -*-
"""Urls for app."""
from django.conf import settings
from django.conf.urls import include, static, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from .api import api_router

from grapple import urls as grapple_urls


urlpatterns = [
    url(r'^django-admin/', admin.site.urls),

    url(r'^api/v2/', api_router.urls),
    url(r"", include(grapple_urls)),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    url(r'', include(wagtail_urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static.static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += (
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
