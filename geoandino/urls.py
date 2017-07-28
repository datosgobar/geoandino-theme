from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from geonode.urls import *
from geoandino.overrides.urls import urlpatterns as override_urls

urlpatterns = patterns('',
   url(r'^/?$',
       TemplateView.as_view(template_name='site_index.html'),
       name='home'),
 ) + override_urls + urlpatterns
