# -*- coding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType 
from django.contrib import admin
from django.core.urlresolvers import reverse
from geoandino.models import SiteConfiguration, ResourceExtra

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

class ResourceExtraAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified', 'resource', 'link_to_resource', 'resource_type', '__str__', )
    list_display = ('__str__', 'super_theme','resource_type','link_to_resource', 'created', 'modified', )
    fieldsets = (
        ('Basic', {
            'fields': ('created', 'modified', )
        }),
        ('data-json', {
            'fields': ('super_theme', ),
        }),
        ('Readonly', {
            'fields': ('link_to_resource', 'resource_type', ),
        }),
    )

    def resource_type(self, obj):
        contenttype = ContentType.objects.get_for_id(obj.resource.polymorphic_ctype_id)
        return contenttype.model

    def link_to_resource(self, obj):
        contenttype = ContentType.objects.get_for_id(obj.resource.polymorphic_ctype_id)
        link=reverse("admin:%s_%s_change" % (contenttype.app_label, contenttype.model), args=[obj.resource.id]) #model name has to be lowercase
        return u'<a href="%s">%s</a>' % (link, obj.resource.title)

    link_to_resource.allow_tags = True

admin.site.register(SiteConfiguration, SiteConfigurationAdmin)
admin.site.register(ResourceExtra, ResourceExtraAdmin)
