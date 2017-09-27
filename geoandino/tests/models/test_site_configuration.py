# -*- coding: utf-8 -*-
from django.test import TestCase
from nose.tools import istest, assert_false, assert_not_equals
from geoandino.tests.test_utils.factories import SiteConfigurationFactory

class TestSiteConfiguration(TestCase):

    def setUp(self):
        self.site_configuration = SiteConfigurationFactory.create()

    @istest
    def site_created_at(self):
        assert self.site_configuration.created

    @istest
    def site_modified(self):
        assert self.site_configuration.modified

    @istest
    def site_title(self):
        assert self.site_configuration.title

    @istest
    def site_description(self):
        assert self.site_configuration.description

    @istest
    def site_is_default(self):
        assert_false(self.site_configuration.default)

    @istest
    def site_publisher(self):
        assert_not_equals(None, self.site_configuration.publisher)