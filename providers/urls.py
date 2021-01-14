from django.urls import path

from providers.views import ProviderDetailView, ProviderListView

# from providers.views import (ProviderCreateView, ProviderDeleteView,
#                              ProviderDetailView, ProviderListView,
#                              ProviderUpdateView)
# urlpatterns = []
urlpatterns = [
    path("", ProviderListView.as_view(), name="provider_list"),
    #     path("add", ProviderCreateView.as_view(), name="add_provider"),
    #     path("edit/<int:pk>/", ProviderUpdateView.as_view(), name="edit_provider"),
    #     path("delete/<int:pk>/", ProviderDeleteView.as_view(), name="delete_provider"),
    path("<int:pk>/", ProviderDetailView.as_view(), name="provider_detail"),
]
