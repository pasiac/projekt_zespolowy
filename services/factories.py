import datetime

import factory
import factory.fuzzy
from factory.django import DjangoModelFactory

from accounts.factories import UserFactory
from services.models import Service
from providers.factories import ProviderFactory


class ServiceFactory(DjangoModelFactory):
    title = factory.Sequence(lambda n: "title_%d" % n)
    # AttributeError: module 'factory' has no attribute 'FuzzyDecimal'
    price = 10.20
    created_by = factory.SubFactory(UserFactory)
    provider = factory.SubFactory(ProviderFactory)

    class Meta:
        model = Service
