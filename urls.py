from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("services/", include("services.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("accounts.urls")),
    path("providers/", include("providers.urls")),
]
