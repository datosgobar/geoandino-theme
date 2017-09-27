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

class ResourceExtra(extension_models.TimeStampedModel):
    resource = models.OneToOneField(ResourceBase,
                        on_delete=models.CASCADE,
                        primary_key=True,
                        related_name="extra_fields",)

    super_theme  = models.CharField(max_length=10, choices=SUPER_THEME_CHOICES, default=get_default_super_theme)

    objects = ResourceExtraManager()

    @property
    def issued(self):
        return self.created.isoformat()

    @property
    def iso_modified(self):
        return self.modified.isoformat()

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


def touch_modified_for_resource(resource):
    ResourceExtra.objects.touch(resource=resource) # Touch "modified" field

def create_resource_extras(instance):
    ResourceExtra.objects.create_for(instance)

def set_default_maintenance_frequency(instance):
    # Taken from from geonode.base.enumerations import UPDATE_FREQUENCIES
    instance.maintenance_frequency = 'continual'
    instance.save()


@receiver(post_save, sender=Layer)
def layer_post_save(sender, instance, created, **kwargs):
    if created:
        create_resource_extras(instance)
        set_default_maintenance_frequency(instance)
    else:
        touch_modified_for_resource(instance)

@receiver(post_save, sender=Document)
def docuemnt_post_save(sender, instance, created, **kwargs):
    if created:
        create_resource_extras(instance)
        set_default_maintenance_frequency(instance)
    else:
        touch_modified_for_resource(instance)

@receiver(post_save, sender=Link)
def create_link_extras(sender, instance, created, **kwargs):
    touch_updated_field(instance, created)
