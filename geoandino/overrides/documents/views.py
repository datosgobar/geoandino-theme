from django.shortcuts import render_to_response
from django.conf import settings
from django.template import RequestContext
try:
    # Django >= 1.7
    import json
except ImportError:
    # Django <= 1.6 backwards compatibility
    from django.utils import simplejson as json

from geonode.documents.views import _resolve_document, _PERMISSION_MSG_METADATA


def document_metadata_detail(request, docid, template='documents/site_metadata_detail.html'):
    document = _resolve_document(
        request,
        docid,
        'view_resourcebase',
        _PERMISSION_MSG_METADATA)
    return render_to_response(template, RequestContext(request, {
        "resource": document,
        'SITEURL': settings.SITEURL[:-1]
}))