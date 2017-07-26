# -*- coding: utf-8 -*-

import factory
from geoandino import models

class SiteConfigurationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.SiteConfiguration

    title = factory.Faker('sentence', nb_words=4)
    description = factory.Faker('text')