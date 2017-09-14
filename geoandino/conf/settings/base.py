# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2016 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################
import os
import environ
from geonode.settings import *

from geoandino.apps.datajsonar.utils.enumerators import SUPER_THEME_CHOICES, AGRI

env = environ.Env()

LANGUAGE_CODE = 'es'

LOCAL_ROOT = environ.Path(__file__) - 3
PROJECT_ROOT = LOCAL_ROOT
PROJECT_DIR = PROJECT_ROOT - 2

WSGI_APPLICATION = "geoandino.wsgi.application"

SITEURL = env("SITEURL", default="http://localhost/")

ALLOWED_HOST = env("ALLOWED_HOST", default="")
ALLOWED_HOST_IP = env("ALLOWED_HOST_IP", default="")

ALLOWED_HOSTS = [
    'localhost', 
    '127.0.0.1',
    'geonode',
    ALLOWED_HOST,
    ALLOWED_HOST_IP,
]
PROXY_ALLOWED_HOSTS = (
    'localhost',
    '127.0.0.1',
    'geonode',
    ALLOWED_HOST,
    ALLOWED_HOST_IP,
)
POSTGIS_VERSION = (2, 1, 2)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('POSTGRES_DB', default=""),
        'USER': env('POSTGRES_USER', default=""),
        'PASSWORD': env('POSTGRES_PASSWORD', default=""),
        'HOST' : env('POSTGRES_HOST', default="db"),
        'PORT' : '5432',
     },
    # vector datastore for uploads
    'datastore' : {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        #'ENGINE': '', # Empty ENGINE name disables
        'NAME': env('DATASTORE_DB', default=""),
        'USER': env('POSTGRES_USER', default=""),
        'PASSWORD': env('POSTGRES_PASSWORD', default=""),
        'HOST' : env('POSTGRES_HOST', default="db"),
        'PORT' : '5432',
    }
}

GEOSERVER_LOCATION = env(
    'GEOSERVER_LOCATION', default='http://geoserver:8080/geoserver/'
)
GEOSERVER_PUBLIC_LOCATION = env(
    'GEOSERVER_PUBLIC_LOCATION', default="%sgeoserver/" % SITEURL
)

# OGC (WMS/WFS/WCS) Server Settings
OGC_SERVER = {
    'default': {
        'BACKEND': 'geonode.geoserver',
        'LOCATION': GEOSERVER_LOCATION,
        'LOGIN_ENDPOINT': 'j_spring_oauth2_geonode_login',
        'LOGOUT_ENDPOINT': 'j_spring_oauth2_geonode_logout',
        # PUBLIC_LOCATION needs to be kept like this because in dev mode
        # the proxy won't work and the integration tests will fail
        # the entire block has to be overridden in the local_settings
        'PUBLIC_LOCATION': GEOSERVER_PUBLIC_LOCATION,
        'USER' : 'admin',
        'PASSWORD' : 'geoserver',
        'MAPFISH_PRINT_ENABLED' : True,
        'PRINT_NG_ENABLED' : True,
        'GEONODE_SECURITY_ENABLED' : True,
        'GEOGIG_ENABLED' : False,
        'WMST_ENABLED' : False,
        'BACKEND_WRITE_ENABLED': True,
        'WPS_ENABLED' : False,
        'LOG_FILE' : '/dev/stdout',
        # Set to dictionary identifier of database containing spatial data in DATABASES dictionary to enable
        'DATASTORE': 'datastore',
    }
}

# If you want to enable Mosaics use the following configuration
#UPLOADER = {
##    'BACKEND': 'geonode.rest',
#    'BACKEND': 'geonode.importer',
#    'OPTIONS': {
#        'TIME_ENABLED': True,
#        'MOSAIC_ENABLED': True,
#        'GEOGIG_ENABLED': False,
#    }
#}

CATALOG_URL = env("CATALOG_URL", default=SITEURL)

CATALOGUE = {
    'default': {
        # The underlying CSW implementation
        # default is pycsw in local mode (tied directly to GeoNode Django DB)
        #'ENGINE': 'geonode.catalogue.backends.pycsw_local',
        # pycsw in non-local mode
        # 'ENGINE': 'geonode.catalogue.backends.pycsw_http',
        # GeoNetwork opensource
        'ENGINE': 'geonode.catalogue.backends.geonetwork',
        # deegree and others
        # 'ENGINE': 'geonode.catalogue.backends.generic',

        # The FULLY QUALIFIED base url to the CSW instance for this GeoNode
        # 'URL': '%scatalogue/csw' % SITEURL,
        'URL': '%sgeonetwork/srv/en/csw' % CATALOG_URL,
        # 'URL': 'http://localhost:8080/deegree-csw-demo-3.0.4/services',

        # login credentials (for GeoNetwork)
        'USER': 'admin',
        'PASSWORD': 'admin',
    }
}

MEDIA_ROOT = env("MEDIA_ROOT", default=PROJECT_DIR("uploaded"))

# Absolute path to the directory that holds static files like app media.
# Example: "/home/media/media.lawrence.com/apps/"
STATIC_ROOT = env("STATIC_ROOT", default=PROJECT_DIR("static_root"))

# Default preview library
#LAYER_PREVIEW_LIBRARY = 'geoext'

# Custom settings

MODIFY_TOPICCATEGORY = True
DEBUG = env("DEBUG", default=False)


LOCAL_GEOSERVER = {
        "source": {
            "ptype": "gxp_wmscsource",
            "url": OGC_SERVER['default']['PUBLIC_LOCATION'] + "wms",
            "restUrl": "/gs/rest"
        }
    }

# Disable by default
DEFAULT_OPENSTREET_MAP = {
        "source": {"ptype": "gxp_osmsource"},
        "type": "OpenLayers.Layer.OSM",
        "name": "mapnik",
        "visibility": True,
        "fixed": True,
        "group": "background"
    }

IGN_GEOSERVER = {
        "source": {"ptype": "gxp_olsource"},
        "type": "OpenLayers.Layer.WMS",
        "args": [
            'ING',
            'http://wms.ign.gob.ar/geoserver/wms',
            {
            'layers': ['capabaseargenmap'],
            "format":"image/png",
            "tiled": True,
            "tilesOrigin": [-20037508.34, -20037508.34],
            },

        ],
        "visibility": True,
        "fixed": True,
        "group": "background",
    }

MAP_BASELAYERS = [
    LOCAL_GEOSERVER,
    {
        "source": {"ptype": "gxp_olsource"},
        "type": "OpenLayers.Layer",
        "args": ["No background"],
        "name": "background",
        "visibility": False,
        "fixed": True,
        "group":"background"
    },
    IGN_GEOSERVER,
]

# Prepending allows to override static files
STATICFILES_DIRS.insert(0, LOCAL_ROOT("static"))

# Location of url mappings
ROOT_URLCONF = 'geoandino.urls'

# Location of locale files
LOCALE_PATHS = (
    LOCAL_ROOT('locale'),
    ) + LOCALE_PATHS

GEOANDINO_APPS = (
    'geoandino',
    'geoandino.apps.datajsonar',
)

INSTALLED_APPS = GEOANDINO_APPS + INSTALLED_APPS

TEMPLATES[0]['DIRS'].insert(0, LOCAL_ROOT("templates"))

TEMPLATES[0]['OPTIONS']['context_processors'].append('geoandino.utils.context_processors.site_conf')
TEMPLATES[0]['OPTIONS']['context_processors'].append('geoandino.utils.context_processors.taxonomies')
TEMPLATES[0]['OPTIONS']['context_processors'].append('geoandino.utils.context_processors.super_theme_taxonomies')
TEMPLATES[0]['OPTIONS']['context_processors'].append('geoandino.utils.context_processors.featured')

MIDDLEWARE_CLASSES += (
    'geoandino.utils.middlewares.ForceDefaultLanguageMiddleware',
)

SUPER_THEME_TAXONOMY_URL = "http://datos.gob.ar/superThemeTaxonomy.json"

DEFAULT_SUPER_THEME = env("DEFAULT_SUPER_THEME_CODE", default=AGRI)

def check_default_super_theme(code):
    if not any(code == super_theme_code for super_theme_code, text in SUPER_THEME_CHOICES):
        raise Exception("Invalid Super Theme code")

check_default_super_theme(DEFAULT_SUPER_THEME)
