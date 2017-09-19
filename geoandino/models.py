# -*- coding: utf-8 -*-
import geoandino.conf.settings.production as settings
import django.db.models as models
from django_extensions.db import models as models_db
from exclusivebooleanfield.fields import ExclusiveBooleanField
from django.utils.translation import ugettext as _
from django.contrib.staticfiles.templatetags.staticfiles import static
from geonode.base.models import TopicCategory
from account.models import EmailAddress
from geonode.groups.models import GroupProfile


AGRI = "agri"
ECON = "econ"
EDUC = "educ"
ENER = "ener"
ENVI = "envi"
GOVE = "gove"
HEAL = "heal"
INTR = "intr"
JUST = "just"
REGI = "regi"
SOCI = "soci"
TECH = "tech"
TRAN = "tran"

# TODO: Use english texts and translated theme
SUPER_THEME_CHOICES = (
    (AGRI, "Agroganadería, pesca y forestación"),
    (ECON, "Economía y finanzas"),
    (EDUC, "Educación, cultura y deportes", ),
    (ENER, "Energía"),    (ENVI, "Medio ambiente"),
    (GOVE, "Gobierno y sector público"),
    (HEAL, "Salud"),
    (INTR, "Asuntos internacionales"),
    (JUST, "Justicia, seguridad y legales"),
    (REGI, "Regiones y ciudades"),
    (SOCI, "Población y sociedad"),
    (TECH, "Ciencia y tecnología"),
    (TRAN, "Transporte"),
)

# Monkey patching to filter datasets by group
#############################################


def add_member_url(username):
    return "owner__username={}".format(username)


def add_members_to_url(search_string, group):
    usernames = list(map(lambda m: m.user.username, group.member_queryset()))
    for username in usernames[:-1]:
        search_string += add_member_url(username)
        search_string += "&"
    search_string += add_member_url(usernames[-1])
    return search_string


@property
def filter_by_group(self):
    search_string = "/search/?limit=100&offset=0&"
    url = add_members_to_url(search_string, self)
    return url


GroupProfile.filter_by_group = filter_by_group

#############################################


def image_url_or_default(self, image_property, default_url):
    image = getattr(self, image_property)
    try:
        return "{}{}".format(settings.SITEURL.rstrip('/'), image.url)
    except ValueError:
        if default_url is None:
            return default_url
        else:
            return static(default_url)


class TopicTaxonomy(models.Model):
    identifier = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default=None, null=True, blank=True)
    limit = models.PositiveIntegerField(default=100)
    offset = models.IntegerField(default=0)
    image = models.ImageField(upload_to="thumbs/", blank=True, null=True)
    icon = models.CharField(max_length=20, default=None, null=True, blank=True)

    class Meta:
        ordering = ['identifier', ]

    @property
    def image_url(self):
        return image_url_or_default(self, 'image', None)

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

    def has_icon(self):
        return True if self.icon else False
    has_icon.boolean = True

    def has_image(self):
        return True if self.image else False
    has_image.boolean = True


class GeoAndinoTopicCategory(TopicCategory):
    def __init__(self, *args, **kwargs):
        self._meta.get_field('identifier').default = None
        super(GeoAndinoTopicCategory, self).__init__(*args, **kwargs)

    topic_taxonomy = models.ForeignKey(TopicTaxonomy, on_delete=models.CASCADE, related_name='topic_categories_set', null=True, blank=True, default=None)


class SiteConfiguration(models_db.TimeStampedModel, models_db.TitleDescriptionModel):
    default = ExclusiveBooleanField(default=False)
    publisher = models.ForeignKey(EmailAddress)
    about_visible = models.BooleanField(default=False, verbose_name=_('Visible'))
    about_title = models.CharField(_('title'), max_length=255, default=None, blank=True, null=True)
    about_description = models.TextField(_('description'), blank=True, null=True)
    image_background = models.ImageField(upload_to="thumbs/", blank=True, null=True, default=None)
    facebook_url = models.CharField(max_length=150, verbose_name=_('Facebook'), default="http://www.facebook.com/portal", null=True, blank=True)
    twitter_url = models.CharField(max_length=150, verbose_name=_('Twitter'), default="http://www.twitter.com/portal", null=True, blank=True)
    github_url = models.CharField(max_length=150, verbose_name=_('GitHub'), default="http://www.github.com/portal", null=True, blank=True)
    contact_mail = models.CharField(max_length=250, verbose_name=_('Contact mail'), default="contact@portal.com", null=True, blank=True)
    layer_description = models.TextField(max_length=250, verbose_name=_('Layer description'), blank=True, null=True)
    map_description = models.TextField(max_length=250, verbose_name=_('Map description'), blank=True, null=True)
    document_description = models.TextField(max_length=250, verbose_name=_('Document description'), blank=True, null=True)
    group_description = models.TextField(max_length=250, verbose_name=_('Group description'), blank=True, null=True)
    group_visible = models.BooleanField(default=False, verbose_name=_('Visible'))
    icon_display = models.BooleanField(default=False, verbose_name=_('Icon display'))
    site_url = models.CharField(_('Site url'), max_length=255, default=None, blank=True, null=True)
    logo_footer = models.ImageField(upload_to="thumbs/", blank=True, null=True)
    logo_header = models.ImageField(upload_to="thumbs/", blank=True, null=True)
    facebook_google_image = models.ImageField(_('Facebook and Google image'), upload_to="thumbs/", blank=True, null=True)
    facebook_google_title = models.CharField(_('Facebook and Google title'), max_length=255, default=None, blank=True, null=True)
    facebook_google_description = models.TextField(_('Facebook and Google description'), blank=True, null=True)
    twitter_image = models.ImageField(_('Twitter image'), upload_to="thumbs/", blank=True, null=True)
    twitter_title = models.CharField(_('Twitter title'), max_length=255, default=None, blank=True, null=True)
    twitter_description = models.TextField(_('Twitter description'), blank=True, null=True)
    twitter_user = models.CharField(_("Twitter user"), max_length=100, null=True, blank=True)

    @property
    def image_background_url(self):
        return image_url_or_default(self, 'image_background', 'img/bg-jumbotron.jpg')

    @property
    def logo_header_url(self):
        return image_url_or_default(self, 'logo_header', 'img/logo_ministerio.svg')

    @property
    def logo_footer_url(self):
        return image_url_or_default(self, 'logo_footer', 'img/argentinagob.svg')

    @property
    def facebook_google_image_url(self):
        return image_url_or_default(self, 'facebook_google_image', None)

    @property
    def twitter_image_url(self):
        return image_url_or_default(self, 'twitter_image', None)

    def publisher_name(self):
        return self.publisher.user.username

    def publisher_email(self):
        return self.publisher.email

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created', ]
