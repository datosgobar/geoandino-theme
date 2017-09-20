# -*- coding: utf-8 -*-
from geoandino.utils.conf import get_site_conf
from geoandino.models import TopicTaxonomy, SUPER_THEME_CHOICES, GroupProfile, GroupTreeNode


def site_conf(request):
    return {"site_conf": get_site_conf()}


def taxonomies(request):
    return {"taxonomies": TopicTaxonomy.objects.all}


def super_theme_taxonomies(request):
    return {"super_theme_taxonomies": SUPER_THEME_CHOICES}


def serializable_nodes():
    serializable = []
    nodes = GroupTreeNode.objects.filter(parent=None)
    for node in nodes:
        serializable.append(node.serializable_object())
    return serializable


def group_nodes(request):
    return {"group_nodes": serializable_nodes()}
