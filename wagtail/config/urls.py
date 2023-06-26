"""Main url routing."""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from interface.api import api_router
from interface.app.views import index

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("admin/", admin.site.urls),
    re_patg(r"^api/v2/", api_router.urls),
    re_path(r"^cms/", include(wagtailadmin_urls)),
    re_path(r"^documents/", include(wagtaildocs_urls)),
    re_path(r"^pages/", include(wagtail_urls)),
    path("", index, name="app"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# catch all for React router
urlpatterns += [re_path(r"^(?:.*)/?$", index)]
