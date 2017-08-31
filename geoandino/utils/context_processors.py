# -*- coding: utf-8 -*-
from geoandino.utils.conf import get_site_conf
from geoandino.models import TopicTaxonomy, SUPER_THEME_CHOICES


def site_conf(request):
    return {"site_conf": get_site_conf()}


def taxonomies(request):
    return {"taxonomies": TopicTaxonomy.objects.all}


def taxonomies_with_data(request):
    return {"taxonomies_with_data": [taxonomy for taxonomy in TopicTaxonomy.objects.all() if taxonomy.referenced_by_data]}


def super_theme_taxonomies(request):
    return {"super_theme_taxonomies": SUPER_THEME_CHOICES}
