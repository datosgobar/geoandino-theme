# -*- coding: utf-8 -*-
from django.conf import settings
from geonode.base.models import ResourceBase
from geonode.maps.models import Map
from geonode.documents.models import Document
from geoandino.utils.conf import get_site_conf


"""
Geonode's /data.json is implemented like:
    json_data = []
    for resource in ResourceBase.objects.all():
        record = {}
        record['title'] = resource.title
        record['description'] = resource.abstract
        record['keyword'] = resource.keyword_csv.split(',')
        record['modified'] = resource.csw_insert_date.isoformat()
        record['publisher'] = resource.poc.organization
        record['contactPoint'] = resource.poc.name_long
        record['mbox'] = resource.poc.email
        record['identifier'] = resource.uuid
        if resource.is_published:
            record['accessLevel'] = 'public'
        else:
            record['accessLevel'] = 'non-public'

        record['distribution'] = []
        for link in resource.link_set.all():
            record['distribution'].append({
                'accessURL': link.url,
                'format': link.mime
            })
        json_data.append(record)

"""
def dataset_from(resource):
    record = {}
    record['title'] = resource.title
    record['description'] = resource.abstract
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