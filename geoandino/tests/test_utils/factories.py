# -*- coding: utf-8 -*-

import factory
from django.contrib.auth import get_user_model
from account import models as account_models
from geoandino import models

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
    username = factory.Sequence(lambda n: 'user%d' % n)
    email = factory.Sequence(lambda n: 'user%d@example.com' % n)

class EmailAddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = account_models.EmailAddress

    user = factory.SubFactory(UserFactory)
    email = factory.Sequence(lambda n: 'emailaccount%d@example.com' % n)

class SiteConfigurationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.SiteConfiguration

    title = factory.Faker('sentence', nb_words=4)
    description = factory.Faker('text')
    publisher = factory.SubFactory(EmailAddressFactory)