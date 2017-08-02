# -*- coding: utf-8 -*-
from django.contrib import admin
from geoandino.models import SiteConfiguration, FacebookAndGoogleMetadata, TwitterMetadata, GeoAndinoTopicCategory, TopicTaxonomy
from django.utils.translation import ugettext as _

from django.forms import ModelMultipleChoiceField, ModelForm


class FacebookAndGoogleMetadataInline(admin.StackedInline):
    model = FacebookAndGoogleMetadata
    max_num = 1
    verbose_name_plural = _('Social Media Metadata')
    verbose_name = _('Facebook and Google')
    fields = ['title', 'description', 'image']


class TwitterMetadataInline(admin.StackedInline):
    model = TwitterMetadata
    max_num = 1
    verbose_name_plural = _('Social Media Metadata')
    verbose_name = _('Twitter')
    fields = ['title', 'description', 'image']


class SiteConfigurationAdmin(admin.ModelAdmin):
    list_display = ('title', 'default')
    fieldsets = [
        (None, {'fields': [_('default')]}),
        (_('Landing'), {'fields': [_('title'), _('description'), _('image_background')]}),
        (_('Header'), {'fields': [_('logo_header')]}),
        (_('Footer'), {'fields': [_('site_url'), _('logo_footer')]}),
        (_('Themes'), {'fields': [_('icon_display')]}),
        (_('Layers, documents and maps'), {'fields': [_('layer_description'), _('document_description'), _('map_description')]}),
        (_('Groups'), {'fields': [_('group_description'), _('group_visible')]}),
        (_('Contact'), {'fields': [_('facebook_url'), _('twitter_url'), _('github_url'), _('instagram_url'), _('youtube_url'), _('contact_mail')]}),
        (_('About (optional)'), {'fields': [_('about_title'), _('about_description'), _('about_visible')]}),
    ]

    inlines = [FacebookAndGoogleMetadataInline, TwitterMetadataInline]


class TopicTaxonomyForm(ModelForm):
    categories = ModelMultipleChoiceField(queryset=GeoAndinoTopicCategory.objects)

    def __init__(self, *args, **kwargs):
        super(TopicTaxonomyForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['categories'].initial = self.instance.topic_categories_set.all()

    def save(self, *args, **kwargs):
        instance = super(TopicTaxonomyForm, self).save(commit=False)
        self.fields['categories'].initial.update(topic_taxonomy=None)
        self.cleaned_data['categories'].update(topic_taxonomy=instance)
        return instance

    class Meta:
        model = TopicTaxonomy
        fields = [_('identifier'), _('description'), _('image')]


class TopicTaxonomyAdmin(admin.ModelAdmin):
    list_display = ('identifier',)
    form = TopicTaxonomyForm


class GeoAndinoTopicCategoryAdmin(admin.ModelAdmin):
    list_display = ('identifier',)
    fields = ['identifier', 'gn_description', 'is_choice', 'fa_class']


admin.site.register(SiteConfiguration, SiteConfigurationAdmin)
admin.site.register(TopicTaxonomy, TopicTaxonomyAdmin)
admin.site.register(GeoAndinoTopicCategory, GeoAndinoTopicCategoryAdmin)
