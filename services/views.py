from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from services.forms import ServiceForm
from services.models import Service


class ServiceListView(LoginRequiredMixin, ListView):
    model = Service
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.order_by("-pk")


class ServiceDetailView(LoginRequiredMixin, DetailView):
    model = Service


class ServiceCreateView(LoginRequiredMixin, CreateView):
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy("owner_service_list")
    extra_context = {"header": "Dodawanie usługi"}

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        provider_pk = self.kwargs.get("pk", "")
        if provider_pk:
            initial['provider'] = provider_pk
        return initial

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        return super().form_valid(form)


class ServiceDeleteView(LoginRequiredMixin, DeleteView):
    model = Service
    success_url = reverse_lazy("owner_service_list")

    # TODO: Create confirmation in js
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class ServiceUpdateView(LoginRequiredMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy("owner_service_list")
    extra_context = {"header": "Edycja usługi"}

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class OwnersServiceListView(LoginRequiredMixin, ListView):
    """ List view of Services that belongs to user """

    model = Service
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.filter(created_by=self.request.user)
