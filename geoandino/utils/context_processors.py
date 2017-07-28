# -*- coding: utf-8 -*-
from geoandino.utils.conf import get_site_conf
from geoandino.models import TopicTaxonomy


def site_conf(request):
    return {"site_conf": get_site_conf()}


def taxonomies(request):
    return {"taxonomies": TopicTaxonomy.objects.all}
