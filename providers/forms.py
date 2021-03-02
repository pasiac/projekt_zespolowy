from django import forms
from django.forms import inlineformset_factory
from providers.models import Provider
from services.models import Service

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from .custom_layout_object import *

class ProviderForm(forms.ModelForm):
    # is_add_services = forms.BooleanField(required=False, label="Add services")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Provider
        exclude = ("user",)


class ProviderFilterForm(forms.ModelForm):
    class Meta:
        model = Provider
        exclude = ("user", "photo", "thumbnail")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].required = False
        self.fields["description"].required = False
        self.fields["services"] = forms.MultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            choices=Service.objects.values_list("pk", "title"),
        )


class ServiceTestform(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ("created_by",)


class ProviderTestForm(forms.ModelForm):
    class Meta:
        model = Provider
        exclude = ['user', ]

    def __init__(self, *args, **kwargs):
        super(ProviderTestForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('name'),
                Field('description'),
                Fieldset('Add services', Formset('services')),
                Field('photo'),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'save')),
                )
            )


ServiceFormSet = inlineformset_factory(Provider, Service, form=ServiceTestform, fields=('title', 'description', 'price'), extra=1, can_delete=True)