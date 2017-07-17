# -*- coding: utf-8 -*-
from geoandino.utils.conf import get_site_conf

def data_jsonar():
    site_conf = get_site_conf()
    """Return data.json(ar) representation of catalogue"""
    return {"title": site_conf.title}