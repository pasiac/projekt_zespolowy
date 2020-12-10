from django.contrib import admin
from providers.models import Provider, ProviderManager

class ProviderAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return ProviderManager.get_queryset(self, request)

admin.site.register(Provider, ProviderAdmin)