from django.conf import settings
import factory
from faker import Factory


faker_provider = Factory.create()

class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = settings.AUTH_USER_MODEL

    username = factory.LazyAttribute(lambda x: faker_provider.name())
    email = factory.LazyAttribute(lambda x: faker_provider.email())
    password = factory.LazyAttribute(lambda x: faker_provider.password())


class CounterFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'counter.Counter'

    user = factory.SubFactory(UserFactory)

