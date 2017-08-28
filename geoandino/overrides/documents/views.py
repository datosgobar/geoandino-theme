from guardian.shortcuts import get_perms

from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.utils.translation import ugettext as _
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.db.models import F

from geonode.security.views import _perms_info_json
from geonode.documents.models import Document
from geonode.documents.models import IMGTYPES
from geonode.utils import build_social_links
from geonode.documents.views import _resolve_document, _PERMISSION_MSG_METADATA, _PERMISSION_MSG_VIEW


def document_detail(request, docid):
    """
    The view that show details of each document
    """
    document = None
    try:
        document = _resolve_document(
            request,
            docid,
            'base.view_resourcebase',
            _PERMISSION_MSG_VIEW)

    except Http404:
        return HttpResponse(
            loader.render_to_string(
                '404.html', RequestContext(
                    request, {
                        })), status=404)

    except PermissionDenied:
        return HttpResponse(
            loader.render_to_string(
                '401.html', RequestContext(
                    request, {
                        'error_message': _("You are not allowed to view this document.")})), status=403)

    if document is None:
        return HttpResponse(
            'An unknown error has occured.',
            content_type="text/plain",
            status=401
        )

    else:
        try:
            related = document.content_type.get_object_for_this_type(
                id=document.object_id)
        except:
            related = ''

        # Update count for popularity ranking,
        # but do not includes admins or resource owners
        if request.user != document.owner and not request.user.is_superuser:
            Document.objects.filter(id=document.id).update(popular_count=F('popular_count') + 1)

        metadata = document.link_set.metadata().filter(
            name__in=settings.DOWNLOAD_FORMATS_METADATA)

        context_dict = {
            'perms_list': get_perms(request.user, document.get_self_resource()),
            'permissions_json': _perms_info_json(document),
            'resource': document,
            'metadata': metadata,
            'imgtypes': IMGTYPES,
            'related': related}

        if settings.SOCIAL_ORIGINS:
            context_dict["social_links"] = build_social_links(request, document)

        if getattr(settings, 'EXIF_ENABLED', False):
            try:
                from geonode.contrib.exif.utils import exif_extract_dict
                exif = exif_extract_dict(document)
                if exif:
                    context_dict['exif_data'] = exif
            except:
                print "Exif extraction failed."

        return render_to_response(
            "documents/site_document_detail.html",
            RequestContext(request, context_dict))


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