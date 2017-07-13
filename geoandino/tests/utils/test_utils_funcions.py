# -*- coding: utf-8 -*-
from nose.tools import istest, assert_true
from django.test import TestCase
from geoandino.utils import conf
from geoandino.tests.test_utils.factories import SiteConfigurationFactory


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

class TestWithDefaultSiteConfiguration(TestWithoutDefaultSiteConfiguration):

    def setUp(self):
        super(TestWithDefaultSiteConfiguration, self).setUp()
        self.site_configuration = self.create_site_configuration()

    def create_site_configuration(self):
        return SiteConfigurationFactory.create()