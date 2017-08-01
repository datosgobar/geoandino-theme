# -*- coding: utf-8 -*-
from django.db import models
from django_extensions.db import models as extension_models
from account.models import EmailAddress

class SiteConfiguration(extension_models.TimeStampedModel, extension_models.TitleDescriptionModel):
    default = models.BooleanField(default=False, )
    publisher = models.ForeignKey(EmailAddress)

    class Meta:
        ordering = ['created', ]

    def publisher_name(self):
        return self.publisher.user.username

    def publisher_email(self):
        return self.publisher.email

    def __str__(self):
        return self.title
