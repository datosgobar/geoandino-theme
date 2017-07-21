from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from geonode.urls import *

urlpatterns = patterns('',
   url(r'^/?$',
       TemplateView.as_view(template_name='site_index.html'),
       name='home'),
    url(r'^layers/?$',
       TemplateView.as_view(template_name='layers/site_layers_list.html'),
       name='layers_browse'),
    url(r'^documents/?$',
       TemplateView.as_view(template_name='documents/site_documents_list.html'),
       name='documents_browse'),
    url(r'^maps/?$',
       TemplateView.as_view(template_name='maps/site_maps_list.html'),
       name='maps_browse'),
    url(r'^groups/?$',
       TemplateView.as_view(template_name='groups/site_groups_list.html'),
       name='groups_browse'),
 ) + urlpatterns
