# -*- coding: utf-8 -*-
from nose.tools import istest, assert_true, assert_equals
from django.test import TestCase
from geoandino.utils.datajsonar import data_jsonar
from geoandino.tests.test_utils.factories import SiteConfigurationFactory


class TestDataJsonAr(TestCase):
    def setUp(self):
        self.site_conf = SiteConfigurationFactory.create(default=True)

    @istest
    def title_is_default_site_confs_title(self):
        title = data_jsonar()['title']
        assert_equals(self.site_conf.title, title)