# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_extensions.db import models as extension_models
from account.models import EmailAddress
from geonode.base.models import ResourceBase
from geonode.layers.models import Layer
from geonode.maps.models import Map
from geonode.documents.models import Document
from geoandino.utils.enumerators import SUPER_THEME_CHOICES
from .managers import ResourceExtraManager


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

@receiver(post_save, sender=Map)
def create_map_extras(sender, instance, created, **kwargs):
    create_resource_extras(instance, created)

@receiver(post_save, sender=Document)
def create_document_extras(sender, instance, created, **kwargs):
    create_resource_extras(instance, created)
