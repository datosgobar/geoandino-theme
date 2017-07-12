# -*- coding: utf-8 -*-
from nose.tools import istest
from django.test import TestCase
from geoandino.utils import conf


class TestWithoutDefaultSiteConfiguration(TestCase):

    def setUp(self):
        self.conf_module = conf

    @istest
    def nullobject_patters(self):
        assert self.conf_module.get_site_conf(), "Always return a site configuration"

    @istest
    def has_title(self):
        assert self.conf_module.get_site_conf().title

    
