from geonode.urls import *
import geoandino.overrides.urls as override_urls
from geoandino.apps.datajsonar.urls import urlpatterns as datajsonar_urls

urlpatterns = override_urls.urlpatterns + datajsonar_urls + urlpatterns
