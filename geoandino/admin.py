# -*- coding: utf-8 -*-
from django.contrib import admin
from geoandino.models import SiteConfiguration, GeoAndinoTopicCategory, TopicTaxonomy
from django.utils.translation import ugettext as _

from django.forms import ModelMultipleChoiceField, ModelForm


class SiteConfigurationAdmin(admin.ModelAdmin):
    list_display = ('title', 'default')
    fieldsets = [
        (None, {'fields': [_('default')]}),
        (_('Landing'), {'fields': ['title',
                                   'description',
                                   'image_background']}),
        (_('Header'), {'fields': ['logo_header']}),
        (_('Footer'), {'fields': ['site_url',
                                  'logo_footer']}),
        (_('Themes'), {'fields': ['icon_display']}),
        (_('Layers, documents and maps'), {'fields': ['layer_description',
                                                      'document_description',
                                                      'map_description']}),
        (_('Groups'), {'fields': ['group_description',
                                  'group_visible']}),
        (_('Contact'), {'fields': ['facebook_url',
                                   'twitter_url',
                                   'github_url',
                                   'instagram_url',
                                   'youtube_url',
                                   'contact_mail']}),
        (_('About (optional)'), {'fields': ['about_title',
                                            'about_description',
                                            'about_visible']}),
        (_('Social media metadata'), {'fields': ['facebook_google_title',
                                                 'facebook_google_description',
                                                 'facebook_google_image',
                                                 'twitter_title',
                                                 'twitter_description',
                                                 'twitter_image',
                                                 'twitter_user']}),
    ]


class TopicTaxonomyForm(ModelForm):
    categories = ModelMultipleChoiceField(queryset=GeoAndinoTopicCategory.objects)

    def __init__(self, *args, **kwargs):
        super(TopicTaxonomyForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['categories'].initial = self.instance.topic_categories_set.all()

    def save(self, *args, **kwargs):
        instance = super(TopicTaxonomyForm, self).save(commit=False)
        instance.save()
        self.fields['categories'].initial.update(topic_taxonomy=None)
        self.cleaned_data['categories'].update(topic_taxonomy=instance)
        return instance

    class Meta:
        model = TopicTaxonomy
        fields = ['identifier', 'description', 'image', 'limit', 'offset']


class TopicTaxonomyAdmin(admin.ModelAdmin):
    list_display = ('identifier',)
    form = TopicTaxonomyForm


class GeoAndinoTopicCategoryAdmin(admin.ModelAdmin):
    list_display = ('identifier',)
    fields = ['identifier', 'gn_description', 'is_choice', 'fa_class']


admin.site.register(SiteConfiguration, SiteConfigurationAdmin)
admin.site.register(TopicTaxonomy, TopicTaxonomyAdmin)
admin.site.register(GeoAndinoTopicCategory, GeoAndinoTopicCategoryAdmin)
