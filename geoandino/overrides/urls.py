# -*- coding: utf-8 -*-

from django.conf.urls import url, patterns
from django.views.generic import TemplateView

from geonode.urls import *

from .views import CreateAnnouncementI18nView, InviteUserI18nView
from django.contrib.auth.decorators import login_required

from geoandino.overrides.documents.views import GeoAndinoDocumentUploadView

# Override geonode's urls with custom views
urlpatterns = patterns(
    "", 
    url(r"^announcements/announcement/create/$", CreateAnnouncementI18nView.as_view(),),
    url(r"^account/invite_user/$", InviteUserI18nView.as_view(),),
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
    url(r'^people/?$',
        TemplateView.as_view(template_name='people/site_profile_list.html'),
        name='people_browse'),
)

layers_urlpatterns = patterns(
                        'geoandino.overrides.layers.views',
                        url(r'^layers/(?P<layername>[^/]*)/metadata$',
                            'layer_metadata',
                            name="layer_metadata"),
                        url(r'^layers/(?P<layername>[^/]*)/metadata_detail$',
                            'layer_metadata_detail',
                            name="layer_metadata_detail"),
                        url(r'^layers/upload$',
                            'layer_upload',
                            name='layer_upload'),
                        url(r'^upload/?$', login_required(GeoAndinoDocumentUploadView.as_view()),
                            name='document_upload'),
                    )

maps_urlpatterns = patterns(
                        'geoandino.overrides.maps.views',
                        url(r'^maps/(?P<mapid>[^/]*)/metadata_detail$',
                            'map_metadata_detail',
                            name="map_metadata_detail"),
                    )

documents_urlpatterns = patterns(
                        'geoandino.overrides.documents.views',
                        url(r'^documents/(?P<docid>[^/]*)/metadata$',
                            'document_metadata',
                            name="document_metadata"),
                        url(r'^documents/(?P<docid>[^/]*)/metadata_detail$',
                            'document_metadata_detail',
                            name="document_metadata_detail"),
                        url(r'^documents/(?P<docid>\d+)/?$',
                            'document_detail',
                            name='document_detail'),
                    )

groups_urlpatterns = patterns(
                        'geoandino.overrides.groups.views',
                        url(r'^groups/group/(?P<slug>[-\w]+)/members/$',
                            'group_members',
                            name="group_members"),
                        url(r'^groups/create/$', 'group_create', name="group_create"),
                        url(r'^groups/group/(?P<slug>[-\w]+)/update/$', 'group_update', name='group_update'),
                    )


urlpatterns = layers_urlpatterns + documents_urlpatterns + maps_urlpatterns + groups_urlpatterns + urlpatterns
