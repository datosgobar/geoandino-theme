# -*- coding: utf-8 -*-
from django.test import TestCase
from nose.tools import istest
from geoandino.models import SiteConfiguration

class TestSiteConfiguration(TestCase):

    def setUp(self):
        self.title = "a title"
        self.description = "a description"
        self.site_configuration = SiteConfiguration.objects.create(title=self.title, description=self.description)

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