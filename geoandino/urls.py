from geonode.urls import *
from geoandino.overrides.urls import urlpatterns as override_urls

from geoandino.apps.datajsonar.urls import urlpatterns as datajsonar_urls

urlpatterns = override_urls + datajsonar_urls + urlpatterns
