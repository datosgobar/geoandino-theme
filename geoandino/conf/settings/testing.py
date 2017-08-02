# -*- coding: utf-8 -*-
from .base import *

CATALOG_URL = "http://geonetwork:8080/"

CATALOGUE['URL'] = '%sgeonetwork/srv/en/csw' % CATALOG_URL
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': ":memory:",
#     },
    # vector datastore for uploads
#    'datastore' : {
#        'ENGINE': 'django.db.backends.sqlite3',
        #'ENGINE': '', # Empty ENGINE name disables
#        'NAME': ":memory:",
#    }
#}
