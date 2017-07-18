# -*- coding: utf-8 -*-
from django.db.models import BooleanField, ForeignKey
from django_extensions.db import models
from account.models import EmailAddress

class SiteConfiguration(models.TimeStampedModel, models.TitleDescriptionModel):
    default = BooleanField(default=False, )
    publisher = ForeignKey(EmailAddress)

    class Meta:
        ordering = ['created', ]