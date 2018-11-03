# -*- coding: utf-8 -*-
"""Urls for app."""
from django.conf import settings
from django.conf.urls import include, static, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import adminactions.actions as actions

actions.add_to_site(admin.site)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/adminactions/', include('adminactions.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static.static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += (
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
