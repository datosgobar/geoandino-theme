# -*- coding: utf-8 -*-
from geoandino.utils.conf import get_site_conf
from geoandino.models import TopicTaxonomy, SUPER_THEME_CHOICES, GroupProfile


def site_conf(request):
    return {"site_conf": get_site_conf()}


def taxonomies(request):
    return {"taxonomies": TopicTaxonomy.objects.all}


def super_theme_taxonomies(request):
    return {"super_theme_taxonomies": SUPER_THEME_CHOICES}


def groups(request):
    return {"groups": GroupProfile.objects.all}
