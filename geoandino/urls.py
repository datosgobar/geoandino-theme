from geonode.urls import *
import geoandino.overrides.urls as override_urls

urlpatterns = override_urls.urlpatterns + override_urls.documents_urlpatterns + urlpatterns
