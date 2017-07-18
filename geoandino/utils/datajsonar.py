# -*- coding: utf-8 -*-
from django.conf import settings
from geonode.base.models import ResourceBase
from geonode.maps.models import Map
from geonode.documents.models import Document
from geoandino.utils.conf import get_site_conf

def dataset_from(resource):
    record = {}
    record['title'] = resource.title
    return record


def get_datasets():
    json_data = []
    for resource in ResourceBase.objects.all():
        json_data.append(dataset_from(resource))
    return json_data

def data_jsonar():
    site_conf = get_site_conf()
    """Return data.json(ar) representation of catalogue"""

    return {
        "title": site_conf.title,
        "description": site_conf.description,
        "publisher": {
            "name": site_conf.publisher.user.username,
            "mbox": site_conf.publisher.email,
        },
        "superThemeTaxonomy": settings.SUPER_THEME_TAXONOMY_URL,
        "datasets": get_datasets(),
    }