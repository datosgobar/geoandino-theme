# -*- coding: utf-8 -*-

from django.db.models.signals import post_save
from django.db import models
from django.dispatch import receiver

from django_extensions.db import models as extension_models
from geonode.base.models import ResourceBase
from geonode.layers.models import Layer
from geonode.documents.models import Document
from .utils.enumerators import SUPER_THEME_CHOICES
from .managers import ResourceExtraManager

class ResourceExtra(extension_models.TimeStampedModel):
    resource = models.OneToOneField(ResourceBase,
                        on_delete=models.CASCADE,
                        primary_key=True,
                        related_name="extra_fields",)
    
    super_theme  = models.CharField(max_length=10, blank=True, null=True, choices=SUPER_THEME_CHOICES, )
    
    objects = ResourceExtraManager()

    def __str__(self):
        if self.resource is not None:
            return self.resource.title
        return super(ResourceExtra, self).__str__()


def create_resource_extras(instance, created):
    if created:
        ResourceExtra.objects.create_for(instance)

@receiver(post_save, sender=Layer)
def create_layer_extras(sender, instance, created, **kwargs):
    create_resource_extras(instance, created)

@receiver(post_save, sender=Document)
def create_document_extras(sender, instance, created, **kwargs):
    create_resource_extras(instance, created)