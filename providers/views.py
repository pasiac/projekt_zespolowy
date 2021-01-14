from django.shortcuts import render

from django.views.generic import ListView, DetailView
from providers.models import Provider

class ProviderListView(ListView):
    model = Provider
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.order_by("-pk")


class ProviderDetailView(DetailView):
    model = Provider

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = self.object.service_set.all()
        return context
