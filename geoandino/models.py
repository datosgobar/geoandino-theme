# -*- coding: utf-8 -*-
import django.db.models as models
from django_extensions.db import models as models_db
from django.utils.translation import ugettext as _


class SiteConfiguration(models_db.TimeStampedModel, models_db.TitleDescriptionModel):
    default = models.BooleanField(default=False)
    about_visible = models.BooleanField(default=False, verbose_name=_('Visible'))
    about_title = models.CharField(_('title'), max_length=255, default=None, blank=True, null=True)
    about_description = models.TextField(_('description'), blank=True, null=True)
    image_background = models.ImageField(blank=True, null=True)
    facebook_url = models.CharField(max_length=150, verbose_name=_('Facebook'), default="www.facebook.com/portal")
    twitter_url = models.CharField(max_length=150, verbose_name=_('Twitter'), default="www.twitter.com/portal")
    github_url = models.CharField(max_length=150, verbose_name=_('GitHub'), default="www.github.com/portal")
    instagram_url = models.CharField(max_length=150, verbose_name=_('Instagram'), default="www.instagram.com/portal")
    youtube_url = models.CharField(max_length=150, verbose_name=_('Youtube'), default="www.youtube.com/portal")
    contact_mail = models.CharField(max_length=250, verbose_name=_('Contact mail'), default="contact@portal.com")
    layer_description = models.TextField(max_length=250, verbose_name=_('Layer description'), blank=True, null=True)
    map_description = models.TextField(max_length=250, verbose_name=_('Map description'), blank=True, null=True)
    document_description = models.TextField(max_length=250, verbose_name=_('Document description'), blank=True, null=True)
    group_description = models.TextField(max_length=250, verbose_name=_('Group description'), blank=True, null=True)
    group_visible = models.BooleanField(default=False, verbose_name=_('Visible'))
    icon_display = models.BooleanField(default=False, verbose_name=_('Icon display'))
    site_url = models.CharField(_('Site url'), max_length=255, default=None, blank=True, null=True)
    logo_footer = models.ImageField(blank=True, null=True)
    logo_header = models.ImageField(blank=True, null=True)

    class Meta:
        ordering = ['created', ]


class FacebookAndGoogleMetadata(models_db.TitleDescriptionModel):
    site_configuration = models.ForeignKey(SiteConfiguration, on_delete=models.CASCADE)
    image = models.ImageField(null=True)

    @classmethod
    def create(cls, site_configuration):
        return cls(site_configuration=site_configuration)


class TwitterMetadata(models_db.TitleDescriptionModel):
    site_configuration = models.ForeignKey(SiteConfiguration, on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    tw_user = models.CharField(max_length=100, verbose_name=_("Twitter User"))

    @classmethod
    def create(cls, site_configuration):
        return cls(site_configuration=site_configuration)




