from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView)

from services.forms import ServiceForm
from services.models import Service


class ServiceListView(ListView):
    model = Service
    paginate_by = 10


class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy("expense_list")
