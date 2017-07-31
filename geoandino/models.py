# -*- coding: utf-8 -*-
import settings
import django.db.models as models
from django_extensions.db import models as models_db
from exclusivebooleanfield.fields import ExclusiveBooleanField
from django.utils.translation import ugettext as _
from django.contrib.staticfiles.templatetags.staticfiles import static
from geonode.base.models import TopicCategory


class TopicTaxonomy(models.Model):
    identifier = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default=None, null=True, blank=True)
    limit = models.PositiveIntegerField(default=100)
    offset = models.IntegerField(default=0)
    image = models.ImageField(upload_to="thumbs/", blank=True, null=True)

    @property
    def image_url(self):
        try:
            return "{}{}".format(settings.SITEURL.rstrip('/'), self.image.url)
        except ValueError:
            return static('img/logo.jpg')

    @property
    def categories(self):
        return self.topic_categories_set.all()

    def identifiers(self):
        topic_categories = self.categories
        return map(lambda topic_category: topic_category.identifier, topic_categories)

    def add_identifier_url(self, identifier):
        return "category__identifier__in={}".format(identifier)

    def add_categories_identifiers_to_url(self, search_string):
        identifiers = self.identifiers()
        for identifier in identifiers[:-1]:
            search_string += self.add_identifier_url(identifier)
            search_string += "&"
        search_string += self.add_identifier_url(identifiers[-1])
        return search_string

    @property
    def search_url(self):
        search_string = "/search/?limit={}&offset={}&".format(self.limit, self.offset)
        return self.add_categories_identifiers_to_url(search_string)


class GeoAndinoTopicCategory(TopicCategory):
    def __init__(self, *args, **kwargs):
        self._meta.get_field('identifier').default = None
        super(GeoAndinoTopicCategory, self).__init__(*args, **kwargs)

    title = models.CharField(max_length=255, default=None, blank=True, null=True)
    topic_taxonomy = models.ForeignKey(TopicTaxonomy, on_delete=models.CASCADE, related_name='topic_categories_set')


class SiteConfiguration(models_db.TimeStampedModel, models_db.TitleDescriptionModel):
    default = ExclusiveBooleanField(default=False)
    about_visible = models.BooleanField(default=False, verbose_name=_('Visible'))
    about_title = models.CharField(_('title'), max_length=255, default=None, blank=True, null=True)
    about_description = models.TextField(_('description'), blank=True, null=True)
    image_background = models.ImageField(upload_to="thumbs/", blank=True, null=True, default=None)
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
    logo_footer = models.ImageField(upload_to="thumbs/", blank=True, null=True)
    logo_header = models.ImageField(upload_to="thumbs/", blank=True, null=True)

    @property
    def image_background_url(self):
        try:
            return "{}{}".format(settings.SITEURL.rstrip('/'), self.image_background.url)
        except ValueError:
            return static('img/bg-jumbotron.jpg')

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




