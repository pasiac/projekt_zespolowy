from django import forms

from providers.models import Provider
from services.models import Service


class ProviderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.pop("user")
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
