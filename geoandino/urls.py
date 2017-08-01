# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from geonode.urls import *
from geoandino.apps.datajsonar.urls import urlpatterns as datajsonar_urls

urlpatterns = patterns('',
   url(r'^/?$', TemplateView.as_view(template_name='site_index.html'), name='home'),
) + datajsonar_urls + urlpatterns
