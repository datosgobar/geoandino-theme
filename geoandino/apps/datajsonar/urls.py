# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import datajsonar

urlpatterns = patterns('',
   url(r'^data.json$', datajsonar, name="datajsonar"),
 )