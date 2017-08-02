# -*- coding: utf-8 -*-

from django.conf import settings
from django.db.models.signals import post_save
from django.db import models
from django.dispatch import receiver
from django.utils.translation import ugettext as _


from django_extensions.db import models as extension_models
from geonode.base.models import ResourceBase, Link
from geonode.layers.models import Layer
from geonode.documents.models import Document
from .utils.enumerators import SUPER_THEME_CHOICES
from .managers import ResourceExtraManager, LinkExtraManager

def get_default_super_theme():
    return settings.DEFAULT_SUPER_THEME

ISO_8601_CONTINUOUSLY_UPDATED = "R/PT1S"

ISO_8601_ACCRUAL_PERIODICITY = [
    ("R/P10Y", _("decennial")),
    ("R/P4Y", _("quadrennial")),
    ("R/P1Y", _("annual")),
    ("R/P2M", _("bimonthly")),
    ("R/P3.5D", _("semiweekly")),
    ("R/P1D", _("daily")),
    ("R/P2W", _("biweekly")),
    ("R/P6M", _("semiannual")),
    ("R/P2Y", _("biennial")),
    ("R/P3Y", _("triennial")),
    ("R/P0.33W", _("three times a week")),
    ("R/P0.33M", _("three times a month")),
    (ISO_8601_CONTINUOUSLY_UPDATED, _("continuously updated")),
    ("R/P1M", _("monthly")),
    ("R/P3M", _("quarterly")),
    ("R/P0.5M", _("semimonthly")),
    ("R/P4M", _("three times a year")),
    ("R/P1W", _("weekly")),
    ("R/PT1H", _("hourly")),
]

class ResourceExtra(extension_models.TimeStampedModel):
    resource = models.OneToOneField(ResourceBase,
                        on_delete=models.CASCADE,
                        primary_key=True,
                        related_name="extra_fields",)
    
    super_theme  = models.CharField(max_length=10, choices=SUPER_THEME_CHOICES, default=get_default_super_theme)
    accrual_periodicity = models.CharField(max_length=10, choices=ISO_8601_ACCRUAL_PERIODICITY, default=ISO_8601_CONTINUOUSLY_UPDATED)
    
    objects = ResourceExtraManager()

    @property
    def issued(self):
        return self.created.isoformat()

    def __str__(self):
        if self.resource is not None:
            return self.resource.title
        return super(ResourceExtra, self).__str__()

class LinkExtra(extension_models.TimeStampedModel):
    link = models.OneToOneField(Link,
                        on_delete=models.CASCADE,
                        primary_key=True,
                        related_name="extra_fields",)

    objects = LinkExtraManager()

    @property
    def issued(self):
        return self.created.isoformat()

def touch_updated_field(instance, created):
    if created:
        LinkExtra.objects.create_for(instance)
    else:
        LinkExtra.objects.get(link=instance).save() # Touch "updated" field

def create_resource_extras(instance, created):
    if created:
        ResourceExtra.objects.create_for(instance)

@receiver(post_save, sender=Layer)
def create_layer_extras(sender, instance, created, **kwargs):
    create_resource_extras(instance, created)

@receiver(post_save, sender=Document)
def create_document_extras(sender, instance, created, **kwargs):
    create_resource_extras(instance, created)

@receiver(post_save, sender=Link)
def create_link_extras(sender, instance, created, **kwargs):
    touch_updated_field(instance, created)