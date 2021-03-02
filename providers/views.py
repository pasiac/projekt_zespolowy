from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView, TemplateView
from django.views.generic.edit import FormMixin
from django.db import transaction

from providers.forms import ProviderForm, ProviderFilterForm, ServiceFormSet, ProviderTestForm
from providers.models import Provider


class ProviderListView(FormMixin, ListView):
    model = Provider
    paginate_by = 10
    form_class = ProviderFilterForm

    def get_queryset(self):
        queryset = self.model.objects.search(**self.request.GET.dict())
        return queryset


class ProviderDetailView(DetailView):
    model = Provider

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = self.object.services.all()
        # if self.object.user == self.request.user:
        #     # Jakaś obsługa tego, że to wchodzi owner
        #     context["cms"] = "Hello"
        return context


class ProviderCreateView(LoginRequiredMixin, CreateView):
    model = Provider
    form_class = ProviderForm
    success_url = reverse_lazy("owners_provider_list")
    extra_context = {"header": "Dodawanie firmy"}

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super().form_valid(form)


class ProviderDeleteView(LoginRequiredMixin, DeleteView):
    model = Provider
    success_url = reverse_lazy("owners_provider_list")

    # TODO: Create confirmation in js
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class OwnersProviderListView(LoginRequiredMixin, ProviderListView):
    """ List view of Providers that belongs to user """

    def get_queryset(self):
        filters = self.request.GET.dict()
        filters["user"] = self.request.user
        return self.model.objects.search(**filters)


class ProviderServicesCreateView(LoginRequiredMixin, CreateView):
    model = Provider
    form_class = ProviderTestForm
    template_name = 'providers/provider_create.html'

    success_url = None
    extra_context = {"header": "Dodawanie firmy"}

    def get_context_data(self, **kwargs):
        data = super(ProviderServicesCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['services'] = ServiceFormSet(self.request.POST)
        else:
            data['services'] = ServiceFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        services = context['services']
        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()
            if services.is_valid():
                services.instance = self.object
                for service in services:
                    service = service.save(commit=False)
                    service.created_by = self.request.user
                # dont increamenting services-TOTAL_FORMS that is probably the case why only one form is being added
                services.save()
        return super(ProviderServicesCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('provider_detail', kwargs={'pk': self.object.pk})