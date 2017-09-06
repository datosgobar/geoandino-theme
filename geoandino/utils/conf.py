# -*- coding: utf-8 -*-

from geoandino.models import SiteConfiguration
from django.contrib.staticfiles.templatetags.staticfiles import static


class NullSiteConfiguration:
    def __init__(self):
        self.title = "Portal Geoandino"
        self.description = "Portal Geoandino"
        self.image_background_url = static('img/bg-jumbotron.jpg')
        self.logo_header_url = static('img/logo_ministerio.svg')
        self.logo_footer_url = static('img/argentinagob.svg')
        self.about_title = 'Acerca de este portal'
        self.about_description = '<b>Describí tu portal con más detalle.</b> ' \
                           'Podés contar cuál es el alcance de los datos geoespaciales que se incluyen.'
        self.default = True
    

def get_nullobject_site_conf():
    return NullSiteConfiguration()


def get_site_conf():
    query = SiteConfiguration.objects.filter(default=True)
    if query.exists():
        return query.first()
    else:
        return get_nullobject_site_conf()
