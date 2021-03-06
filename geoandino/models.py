# -*- coding: utf-8 -*-
import geoandino.conf.settings.production as settings
import django.db.models as models
from django_extensions.db import models as models_db
from exclusivebooleanfield.fields import ExclusiveBooleanField
from django.utils.translation import ugettext as _
from django.contrib.staticfiles.templatetags.staticfiles import static
from geonode.base.models import TopicCategory, ResourceBase
from geonode.layers.models import Layer
from geonode.documents.models import Document
from account.models import EmailAddress
from geonode.groups.models import GroupProfile
from django.db.models.signals import pre_save, post_save, post_delete
from ckeditor.fields import RichTextField
import re


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
    description = models.TextField(default=None, null=True, blank=True)
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

    @property
    def referenced_by_data(self):
        return any(category.referenced_by_data() for category in self.categories)

    @property
    def get_description(self):
        return self.description or self.categories[0].description


class GeoAndinoTopicCategory(TopicCategory):
    def __init__(self, *args, **kwargs):
        self._meta.get_field('identifier').default = None
        super(GeoAndinoTopicCategory, self).__init__(*args, **kwargs)

    topic_taxonomy = models.ForeignKey(TopicTaxonomy, on_delete=models.SET_NULL, related_name='topic_categories_set', null=True, blank=True, default=None)

    def referenced_by_layer(self):
        return Layer.objects.filter(category=self).exists()

    def referenced_by_document(self):
        return Document.objects.filter(category=self).exists()

    def referenced_by_data(self):
        return self.referenced_by_document() or self.referenced_by_layer()


class SiteConfiguration(models_db.TimeStampedModel, models_db.TitleDescriptionModel):
    default = ExclusiveBooleanField(default=False)
    publisher = models.ForeignKey(EmailAddress)
    about_visible = models.BooleanField(default=False, verbose_name=_('Visible'))
    about_title = models.CharField(_('title'), max_length=255, default=None, blank=True, null=True)
    about_description = RichTextField(verbose_name=_('description'), null=True, default=None)
    image_background = models.ImageField(_('Image background'), upload_to="thumbs/", blank=True, null=True, default=None)
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
    logo_footer = models.ImageField(_('Logo footer'), upload_to="thumbs/", blank=True, null=True)
    logo_header = models.ImageField(_('Logo header'), upload_to="thumbs/", blank=True, null=True)
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


class GroupTreeNode(models.Model):
    group = models.OneToOneField(GroupProfile, on_delete=models.CASCADE)
    children_nodes = models.ForeignKey('self',
                                       on_delete=models.CASCADE,
                                       null=True,
                                       related_name='children')
    parent = models.OneToOneField('self', null=True, default=None, on_delete=models.CASCADE)

    @property
    def title(self):
        return self.group.title

    def usernames(self):
        return list(map(lambda m: m.user.username, self.group.member_queryset()))

    def remove_repeted(self, usernames, search_string):
        new_usernames = []
        used_usernames = re.findall("owner__username__in=([\w]*)&?", search_string)
        for username in usernames:
            if username not in used_usernames:
                new_usernames.append(username)
        return new_usernames

    def add_member_url(self, username):
        return "owner__username__in={}".format(username)

    def add_members_to_url(self, search_string, usernames):
        new_usernames = self.remove_repeted(usernames, search_string)
        if new_usernames:
            search_string += "&"
            for username in new_usernames[:-1]:
                search_string += self.add_member_url(username)
                search_string += "&"
            search_string += self.add_member_url(new_usernames[-1])
        return search_string

    def all_children(self):
        descendants = []
        for child in self.children.all():
            descendants.append(child)
            if child.children.all():
                descendants += child.all_children()
        return descendants

    def filter_by_group(self, search_string):
        return self.add_members_to_url(search_string, self.usernames())

    @property
    def filter_by_group_tree(self):
        search_string = "/search/?limit=100&offset=0"
        search_string = self.filter_by_group(search_string)
        children = self.all_children()
        if children:
            for child in children[:-1]:
                search_string = child.filter_by_group(search_string)
            search_string = children[-1].filter_by_group(search_string)
        return search_string

    def serialize_group(self):
        return {'id': self.group.id, 'filter_url': self.filter_by_group_tree}

    def serializable_object(self):
        obj = {'title': self.title,
               'children': [],
               'has_parent': self.parent is not None,
               'group': self.serialize_group()}
        for child in self.children.all():
            obj['children'].append(child.serializable_object())
        return obj

    class Meta:
        ordering = ['group__title']


def add_http(sender, instance, **kwargs):
    site_url = instance.site_url
    if site_url and not site_url.startswith("http"):
        instance.site_url = "http://{}".format(site_url)


def create_group_node(sender, instance, created, **kwargs):
    if created:
        GroupTreeNode.objects.create(group=instance)


def delete_group(sender, instance, **kwargs):
        GroupProfile.objects.filter(title=instance.title).first().delete()


def default_message(abstract):
    return abstract == 'No abstract provided' or abstract == _('No abstract provided')


def update_abstract(sender, instance, created, **kwargs):
    if created and default_message(instance.abstract):
        instance.abstract = ' '


pre_save.connect(add_http, sender=SiteConfiguration)
post_save.connect(create_group_node, sender=GroupProfile)
post_delete.connect(delete_group, sender=GroupTreeNode)
post_save.connect(update_abstract, sender=Document)
