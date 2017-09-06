from geonode.urls import *
import geoandino.overrides.urls as override_urls

urlpatterns = override_urls.urlpatterns + \
              override_urls.layers_urlpatterns + \
              override_urls.maps_urlpatterns + \
              override_urls.documents_urlpatterns + \
              override_urls.groups_urlpatterns + \
              urlpatterns

