# -*- coding: utf-8 -*-
from django.db.models import BooleanField
from django_extensions.db import models

class SiteConfiguration(models.TimeStampedModel, models.TitleDescriptionModel):
    default = BooleanField(default=False, )

    class Meta:
        ordering = ['created', ]