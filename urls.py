from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = [
    path("admin/", admin.site.urls),
    path("services/", include("services.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("account/", include("accounts.urls")),
    path("", include("providers.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
