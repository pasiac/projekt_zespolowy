from django import forms
from providers.models import Provider


class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        exclude = ("user",)
