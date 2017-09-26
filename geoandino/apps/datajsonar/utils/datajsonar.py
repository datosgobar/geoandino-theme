# -*- coding: utf-8 -*-
from django.conf import settings
from geonode.base.models import ResourceBase
from geonode.documents.models import Document
from geonode.layers.models import Layer

from geoandino.utils.conf import get_site_conf
from .enumerators import ACCRUAL_PERIODICITY_DICT


def get_access_url(resource, link):
    links = [link for link in resource.link_set.all() if link.link_type == "html"]
    if links:
        return links[0].url
    return link.url


def translate_accrual_periodicity(string):
    return ACCRUAL_PERIODICITY_DICT.get(string, "")


def distribution_from(resource, link):
    return {
        "accessURL": get_access_url(resource, link),
        "downloadURL": link.url,
        "title": "%s (%s)" % (resource.title, link.name),
        "issued": link.extra_fields.issued
    }


def is_valid_for_datajson(link):
    if link.extension == "tiles":
        return False
    return True


def get_distributions(resource):
    distributions = []
    for link in resource.link_set.all():
        if is_valid_for_datajson(link):
            distributions.append(distribution_from(resource, link))
    return distributions


def dataset_from(resource):
    record = {}
    resource_extras = resource.extra_fields
    record['title'] = resource.title
    record['description'] = resource.abstract
    record['issued'] = resource_extras.issued
    record['modified'] = resource.csw_insert_date.isoformat()
    record['identifier'] = resource.uuid
    record['superTheme'] = [resource_extras.super_theme]
    record['accrualPeriodicity'] = translate_accrual_periodicity(resource.maintenance_frequency)
    record['publisher'] = {
        "name": resource.poc.get_full_name(),
        "mbox": resource.poc.email,
    }
    distributions = get_distributions(resource)
    record['distribution'] = distributions
    if distributions:
        landingPage = distributions[0]["accessURL"]
    else:
        landingPage = "" # Can this happen?
    record["landingPage"] = landingPage
    return record


def get_datasets():
    json_data = []
    base_query = ResourceBase.objects.select_related("owner"). \
        prefetch_related("link_set").select_related("extra_fields").all()
    query = base_query.instance_of(Layer) | base_query.instance_of(Document)
    for resource in query:
        json_data.append(dataset_from(resource))
    return json_data


def data_jsonar():
    site_conf = get_site_conf()
    """Return data.json(ar) representation of catalogue"""

    return {
        "title": site_conf.title,
        "description": site_conf.description,
        "publisher": {
            "name": site_conf.publisher_name(),
            "mbox": site_conf.publisher_email(),
        },
        "superThemeTaxonomy": settings.SUPER_THEME_TAXONOMY_URL,
        "dataset": get_datasets(),
    }
