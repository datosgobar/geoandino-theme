# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from geonode.urls import *
from geoandino.views import data_json

urlpatterns = patterns('',
   url(r'^data.json$', data_json, name="data_jsonar"),
   url(r'^/?$',
       TemplateView.as_view(template_name='site_index.html'),
       name='home'),
 ) + urlpatterns
