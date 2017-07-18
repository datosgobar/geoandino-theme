# -*- coding: utf-8 -*-
from nose.tools import istest, assert_true, assert_equals
from django.test import TestCase
from django.conf import settings
from geoandino.utils.datajsonar import data_jsonar
from geoandino.tests.test_utils.factories import SiteConfigurationFactory


class TestDataJsonAr(TestCase):
    def setUp(self):
        self.site_conf = SiteConfigurationFactory.create(default=True)
        self.settings = settings

    @istest
    def title_from_site_conf(self):
        title = data_jsonar()['title']
        assert_equals(self.site_conf.title, title)

    @istest
    def description_from_site_conf(self):
        description = data_jsonar()['description']
        assert_equals(self.site_conf.description, description)

    @istest
    def publisher_name_from_site_conf(self):
        publisher_name = data_jsonar()['publisher']['name']
        assert_equals(self.site_conf.publisher.user.username, publisher_name)

    @istest
    def publisher_mbox_from_site_conf(self):
        publisher_mbox = data_jsonar()['publisher']['mbox']
        assert_equals(self.site_conf.publisher.email, publisher_mbox)

    @istest
    def super_theme_taxonomy_from_settigs(self):
        taxonomy = data_jsonar()['superThemeTaxonomy']
        assert_equals(self.settings.SUPER_THEME_TAXONOMY_URL, taxonomy)

