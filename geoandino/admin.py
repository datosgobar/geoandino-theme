# -*- coding: utf-8 -*-

from django.contrib import admin
from geoandino.models import SiteConfiguration

class SiteConfigurationAdmin(admin.ModelAdmin):
    list_display = ('title', 'default', 'publisher',)
    fieldsets = (
        ('Basic', {
            'fields': ('title', 'description', 'default')
        }),
        ('Data Jsonar', {
            'classes': ('collapse',),
            'fields': ('publisher', ),
        }),
    )

admin.site.register(SiteConfiguration, SiteConfigurationAdmin)
