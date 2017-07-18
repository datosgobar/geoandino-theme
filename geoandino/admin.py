# -*- coding: utf-8 -*-

from django.contrib import admin
from geoandino.models import SiteConfiguration
from django.utils.translation import ugettext as _


class SiteConfigurationAdmin(admin.ModelAdmin):
    list_display = ('title', 'default')

    fieldsets = [
        (_('Landing'), {'fields': [_('title'), _('description'), _('default')]}),
        (_('About (opcional)'), {'fields': [_('about_title'), _('about_description'), _('about_visible')]}),
    ]

admin.site.register(SiteConfiguration, SiteConfigurationAdmin)
