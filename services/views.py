from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView)

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
    success_url = reverse_lazy("service_list")
    extra_context = {"header": "Dodawanie usługi"}

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.created_by = self.request.user
        return super().form_valid(form)


class ServiceDeleteView(LoginRequiredMixin, DeleteView):
    model = Service
    success_url = reverse_lazy("service_list")

    # TODO: Create confirmation in js
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class ServiceUpdateView(LoginRequiredMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy("service_list")
    extra_context = {"header": "Edycja usługi"}
