# -*- coding: utf-8 -*-
from geoandino.utils.conf import get_site_conf
from geoandino.models import TopicTaxonomy, GroupTreeNode
from geoandino.models import TopicTaxonomy
from geonode.base.models import ResourceBase
from django.conf import settings


def site_conf(request):
    return {"site_conf": get_site_conf()}


def taxonomies(request):
    return {"taxonomies": TopicTaxonomy.objects.all}


def serializable_nodes():
    serializable = []
    nodes = GroupTreeNode.objects.filter(parent=None)
    for node in nodes:
        serializable.append(node.serializable_object())
    return serializable


def group_nodes(request):
    return {"group_nodes": serializable_nodes()}


def taxonomies_with_data(request):
    return {"taxonomies_with_data": [taxonomy for taxonomy in TopicTaxonomy.objects.all() if taxonomy.referenced_by_data]}


def featured(request):
    queryset = ResourceBase.objects.filter(featured=True).order_by('-date')
    if settings.RESOURCE_PUBLISHING:
        queryset = queryset.filter(is_published=True)
    return {"featured": queryset}
