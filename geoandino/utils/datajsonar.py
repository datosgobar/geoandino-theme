# -*- coding: utf-8 -*-
from django.conf import settings
from geonode.base.models import ResourceBase
from geonode.maps.models import Map
from geonode.layers.models import Layer
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

ISO_8601_ACCRUAL_PERIODICITY_DIC = {
    "decennial":	"R/P10Y",
    "quadrennial":	"R/P4Y",
    "annual":	"R/P1Y",
    "bimonthly":	"R/P2M",
    "semiweekly":	"R/P3.5D",
    "daily":	"R/P1D",
    "biweekly":	"R/P2W",
    "semiannual":	"R/P6M",
    "biennial":	"R/P2Y",
    "triennial":	"R/P3Y",
    "three_times_a_week":	"R/P0.33W",
    "three_times_a_month":	"R/P0.33M",
    "continuously_updated":	"R/PT1S",
    "monthly":	"R/P1M",
    "quarterly":	"R/P3M",
    "semimonthly":	"R/P0.5M",
    "three_times_a_year":	"R/P4M",
    "weekly":	"R/P1W",
    "hourly":	"R/PT1H",
}

# Keys taken from geonode.base.enumerators.UPDATE_FREQUENCIES
GEONODE_MAINTENANCE_FREQUENCIES_DIC = {
    "continual": ISO_8601_ACCRUAL_PERIODICITY_DIC['continuously_updated'],
    "daily": ISO_8601_ACCRUAL_PERIODICITY_DIC['daily'],
    "annualy": ISO_8601_ACCRUAL_PERIODICITY_DIC['annual'],
    "monthly": ISO_8601_ACCRUAL_PERIODICITY_DIC['monthly'],
    "fortnightly": ISO_8601_ACCRUAL_PERIODICITY_DIC['biweekly'],
    "weekly": ISO_8601_ACCRUAL_PERIODICITY_DIC['weekly'],
    "biannually": ISO_8601_ACCRUAL_PERIODICITY_DIC['semiannual'],
    "quarterly": ISO_8601_ACCRUAL_PERIODICITY_DIC['quarterly'],
}

def string_to_accrual_periodicity(value):
    # Tanslate *known* values to ISO 8601, otherwise return an empty string
    # Taken from https://project-open-data.cio.gov/iso8601_guidance/
    return GEONODE_MAINTENANCE_FREQUENCIES_DIC.get(value, "")

def get_access_url(resource, link):
    links = [link for link in resource.link_set.all() if link.link_type == "html"]
    if links:
        return links[0].url
    return link.url


def distribution_from(resource, link):
    return {
        "accessURL": get_access_url(resource, link),
        "downloadURL": link.url,
        "title": link.name,
    }

def get_distributions(resource):
    distributions = []
    for link in resource.link_set.all():
        distributions.append(distribution_from(resource, link))
    return distributions

def dataset_from(resource):
    record = {}
    resource_extras = resource.extra_fields
    record['title'] = resource.title
    record['description'] = resource.abstract
    record['issued'] = resource_extras.created
    record['superTheme'] = resource_extras.super_theme
    record['accrualPeriodicity'] = string_to_accrual_periodicity(resource.maintenance_frequency)
    record['publisher'] = {
        "name": resource.poc.get_full_name(),
        "mbox": resource.poc.email,
    }
    record['distribution'] = get_distributions(resource)
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