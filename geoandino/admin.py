# -*- coding: utf-8 -*-

from django.contrib import admin
from geoandino.models import SiteConfiguration

class SiteConfigurationAdmin(admin.ModelAdmin):
    list_display = ('title', 'default', )

admin.site.register(SiteConfiguration, SiteConfigurationAdmin)
