from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView

from providers.forms import ProviderForm
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
        # if self.object.user == self.request.user:
        #     # Jakaś obsługa tego, że to wchodzi owner
        #     context["cms"] = "Hello"
        return context


class ProviderCreateView(LoginRequiredMixin, CreateView):
    model = Provider
    form_class = ProviderForm
    success_url = reverse_lazy("owners_provider_list")
    extra_context = {"header": "Dodawanie firmy"}


class ProviderDeleteView(LoginRequiredMixin, DeleteView):
    model = Provider
    success_url = reverse_lazy("owners_provider_list")

    # TODO: Create confirmation in js
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class OwnersProviderListView(LoginRequiredMixin, ListView):
    """ List view of Providers that belongs to user """
    model = Provider
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
