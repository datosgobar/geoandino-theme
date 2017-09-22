from django.shortcuts import render_to_response
from django.conf import settings
from django.template import RequestContext
from django.http import HttpResponse
try:
    # Django >= 1.7
    import json
except ImportError:
    # Django <= 1.6 backwards compatibility
    from django.utils import simplejson as json

from geonode.maps.views import _resolve_map, new_map_config


def map_metadata_detail(request, mapid, template='maps/site_metadata_detail.html'):
    map_obj = _resolve_map(request, mapid, 'view_resourcebase')
    return render_to_response(template, RequestContext(request, {
        "resource": map_obj,
        'SITEURL': settings.SITEURL[:-1]
}))


def new_map(request, template='maps/site_map_new.html'):
    config = new_map_config(request)
    context_dict = {
        'config': config,
    }
    context_dict["preview"] = getattr(
        settings,
        'LAYER_PREVIEW_LIBRARY',
        '')
    if isinstance(config, HttpResponse):
        return config
    else:
        return render_to_response(template, RequestContext(request, context_dict))

