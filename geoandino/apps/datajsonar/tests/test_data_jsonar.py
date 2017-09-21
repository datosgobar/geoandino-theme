# -*- coding: utf-8 -*-

from django.conf import settings
from django.test import TestCase
from geonode.base.populate_test_data import create_models
from geonode.documents.models import Document
from geonode.layers.models import Layer
from nose.tools import istest, assert_true, assert_equals, assert_not_equals, assert_false
from pydatajson import DataJson

from geoandino.tests.test_utils.factories import SiteConfigurationFactory, LinkFactory
from ..models import get_default_super_theme
from ..utils.datajsonar import (data_jsonar, dataset_from, distribution_from, get_access_url,
                                translate_accrual_periodicity, is_valid_for_datajson)
from ..utils.enumerators import AGRI


class TestDataJsonAr(TestCase):
    # Required by create_models() function, from geonode's initial_data.json
    fixtures = ['initial_data.json']

    def setUp(self):
        self.site_conf = SiteConfigurationFactory.create(default=True)
        self.settings = settings

    @istest
    def has_datajsonar_attributes(self):
        data = data_jsonar()
        expected = {
            "title": self.site_conf.title,
            "description": self.site_conf.description,
            "publisher": {
                "name": self.site_conf.publisher.user.username,
                "mbox": self.site_conf.publisher.email,
            },
            "superThemeTaxonomy": self.settings.SUPER_THEME_TAXONOMY_URL,
            "dataset": []
        }
        for key, value in expected.iteritems():
            assert_equals(value, data[key])

    @istest
    def dataset_from_layers(self):
        create_models(type='layer')
        datasets = data_jsonar()['dataset']
        assert_equals(Layer.objects.count(), len(datasets))

    @istest
    def maps_does_not_create_datasets(self):
        create_models(type='map')
        datasets = data_jsonar()['dataset']
        assert_equals(0, len(datasets))

    @istest
    def dataset_from_layers_and_documents(self):
        create_models(type='layer')
        create_models(type='document')
        expected_count = Layer.objects.count() + Document.objects.count()
        datasets = data_jsonar()['dataset']
        assert_equals(expected_count, len(datasets))

    @istest
    def validate_pydatajson(self):
        create_models(type='layer')
        create_models(type='document')
        catalog = data_jsonar()
        dj = DataJson()
        assert_true(dj.is_valid_catalog(catalog), dj.validate_catalog(catalog))


class DataJsonArDatasetMixin:
    # Required by create_models() function, from geonode's initial_data.json
    fixtures = ['initial_data.json']

    def setUp(self):
        self.site_conf = SiteConfigurationFactory.create(default=True)
        self.settings = settings
        self.create_models()

    def create_models(self):
        raise NotImplementedError("This should be implement in a subclass.")

    def get_models(self):
        raise NotImplementedError("This should be implement in a subclass.")

    def get_model(self):
        return self.get_models().first()

    def get_AGRI_model(self):
        model = self.get_model()
        model.extra_fields.super_theme = AGRI
        model.extra_fields.save()
        return model

    def test_has_datajsonar_attributes(self):
        model = self.get_models().first()
        dataset = dataset_from(model)
        expected = {
            "title": model.title,
            "description": model.abstract,
            "identifier": model.uuid,
            "accrualPeriodicity": translate_accrual_periodicity(model.maintenance_frequency),
            "publisher": {
                "name": model.poc.get_full_name(),
                "mbox": model.poc.email,
            },
            "landingPage": get_access_url(model, None), # <-- I'm assumming at least one Link here
            "modified": model.csw_insert_date.isoformat(),
            "issued": model.extra_fields.issued,
            "superTheme": [get_default_super_theme()],
        }
        for key, value in expected.iteritems():
            assert_equals(value, dataset[key])

    def test_has_attributes(self):
        model = self.get_models().first()
        dataset = dataset_from(model)
        expected = ['distribution']
        for key in expected:
            assert_true(key in dataset)

    def test_has_super_theme(self):
        model = self.get_AGRI_model()
        dataset = dataset_from(model)
        assert_equals([model.extra_fields.super_theme], dataset['superTheme'])

    def test_has_accrual_periodicity(self):
        model = self.get_model()
        dataset = dataset_from(model)
        assert_not_equals(None, dataset['accrualPeriodicity'])
        assert_not_equals("", dataset['accrualPeriodicity'])


class DataJsonArDistributionMixin:
    def get_samples(self):
        model = self.get_model()
        return model, LinkFactory.create(resource=model)

    def test_has_datajsonar_attributes_for_distribution(self):
        resource, link = self.get_samples()
        distribution = distribution_from(resource, link)
        expected = {
            "accessURL": get_access_url(resource, link),
            "downloadURL": link.url,
            "title": link.name,
            "issued": link.extra_fields.issued,
        }
        for key, value in expected.iteritems():
            assert_equals(value, distribution[key])

    def test_tiles_are_invalid(self):
        resource, link = self.get_samples()
        assert_true(is_valid_for_datajson(link))
        link.extension = "tiles"
        assert_false(is_valid_for_datajson(link))


class TestDataJsonArDatasetFromDocuments(DataJsonArDatasetMixin, DataJsonArDistributionMixin, TestCase):
    def create_models(self):
        create_models(type='document')

    def get_models(self):
        return Document.objects.all()


class TestDataJsonArDatasetFromLayers(DataJsonArDatasetMixin, DataJsonArDistributionMixin, TestCase):
    def test_has_attributes(self):
        model = self.get_models().first()

        dataset = dataset_from(model)
        expected = ['distribution']
        for key in expected:
            assert_true(key in dataset)

    def create_models(self):
        create_models(type='layer')

    def get_models(self):
        return Layer.objects.all()
