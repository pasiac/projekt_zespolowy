from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from providers.forms import ProviderForm
from django.views.generic import ListView, DetailView, CreateView
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

class ProviderCreateView(LoginRequiredMixin, CreateView):
    model = Provider
    form_class = ProviderForm
    success_url = reverse_lazy("provider_list")
    extra_context = {"header": "Dodawanie firmy"}