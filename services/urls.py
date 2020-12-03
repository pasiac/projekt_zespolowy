from django.urls import path

from services.views import ServiceCreateView, ServiceListView, ServiceDeleteView, ServiceUpdateView, ServiceDetailView

urlpatterns = [
    path("", ServiceListView.as_view(), name="service_list"),
    path("add", ServiceCreateView.as_view(), name="add_service"),
    path("edit/<int:pk>/", ServiceUpdateView.as_view(), name="edit_service"),
    path("delete/<int:pk>/", ServiceDeleteView.as_view(), name="delete_service"),
    path("<int:pk>/", ExpenseDetailView.as_view(), name="expense_detail"),

]
