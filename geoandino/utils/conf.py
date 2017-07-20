# -*- coding: utf-8 -*-

from geoandino.models import SiteConfiguration

class NullSiteConfiguration:
    def __init__(self):
        self.title = "Portal Geoandino"
        self.description = "Portal Geoandino"
        self.default = True

    def publisher_name(self):
        return "%s's admin" % self.title

    def publisher_email(self):
        return "admin@example.com"
    

def get_nullobject_site_conf():
    return NullSiteConfiguration()

def get_site_conf():
    query = SiteConfiguration.objects.select_related("publisher__user").filter(default=True)
    if query.exists():
        return query.first()
    else:
        return get_nullobject_site_conf()
