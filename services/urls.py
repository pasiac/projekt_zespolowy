from django.urls import path

from services.views import ServiceCreateView, ServiceListView

urlpatterns = [
    path("", ServiceListView.as_view(), name="service_list"),
    path("dodaj", ServiceCreateView.as_view(), name="add_service"),
]
