from geonode.urls import *
from geoandino.overrides.urls import urlpatterns as override_urls

urlpatterns = override_urls + urlpatterns
