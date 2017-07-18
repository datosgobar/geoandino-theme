# -*- coding: utf-8 -*-
import django.db.models as models
from django_extensions.db import models as models_db
from django.utils.translation import ugettext as _


class SiteConfiguration(models_db.TimeStampedModel, models_db.TitleDescriptionModel):
    default = models.BooleanField(default=False, )
    about_visible = models.BooleanField(default=False, verbose_name=_('Visible'))
    about_title = models.CharField(_('title'), max_length=255)
    about_description = models.TextField(_('description'), blank=True, null=True)

    class Meta:
        ordering = ['created', ]