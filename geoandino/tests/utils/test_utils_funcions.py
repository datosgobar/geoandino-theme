# -*- coding: utf-8 -*-
from nose.tools import istest, assert_true
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

    @istest
    def has_description(self):
        assert self.conf_module.get_site_conf().description

    @istest
    def has_default_boolean(self):
        assert_true(self.conf_module.get_site_conf().default)
