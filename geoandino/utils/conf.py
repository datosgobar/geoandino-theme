# -*- coding: utf-8 -*-

from geoandino.models import SiteConfiguration

class NullSiteConfiguration:
    def __init__(self):
        self.title = "Portal Geoandino"
        self.description = "Portal Geoandino"
        self.default = True
    

def get_nullobject_site_conf():
    return NullSiteConfiguration()

def get_site_conf():
    query = SiteConfiguration.objects.filter(default=True)
    if query.exists():
        return query.first()
    else:
        return get_nullobject_site_conf()
