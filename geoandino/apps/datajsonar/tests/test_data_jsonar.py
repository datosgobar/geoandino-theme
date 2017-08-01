# -*- coding: utf-8 -*-
from nose.tools import istest, assert_true, assert_equals
from django.test import TestCase
from django.conf import settings
from parameterized import parameterized
from geonode.base.populate_test_data import create_models
from geonode.layers.models import Layer
from geonode.maps.models import Map
from geonode.documents.models import Document
from geoandino.tests.test_utils.factories import SiteConfigurationFactory, TopicCategoryFactory, a_word, LinkFactory
from ..utils.enumerators import AGRI
from ..utils.datajsonar import (data_jsonar, dataset_from, string_to_accrual_periodicity, 
                                        ISO_8601_ACCRUAL_PERIODICITY_DIC, distribution_from, get_access_url, )


class TestDataJsonAr(TestCase):

    # Required by create_models() function, from geonode's initial_data.json
    fixtures = ['initial_data.json']

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

    @istest
    def has_dataset_list(self):
        datasets = data_jsonar()['dataset']
        assert_equals([], datasets)

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

class TestStringToAccrualPeriodicity:

    @parameterized.expand([
        ("continual", "continuously_updated"),
        ("daily", "daily"),
        ("annualy", "annual"),
        ("monthly", "monthly"),
        ("fortnightly", "biweekly"),
        ("weekly", "weekly"),
        ("biannually", "semiannual"),
        ("quarterly", "quarterly"),
    ])
    def test_periodicity_mapping(self, geonode_value, iso_8601_key):
        iso_formated = string_to_accrual_periodicity(geonode_value)
        expected = ISO_8601_ACCRUAL_PERIODICITY_DIC[iso_8601_key]
        assert_equals(expected, iso_formated)

    def test_periodicity_mapping_with_invalid_value(self):
        iso_formated = string_to_accrual_periodicity(a_word())
        assert_equals("", iso_formated)

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

    def test_has_title(self):
        model = self.get_models().first()
        dataset = dataset_from(model)
        assert_equals(model.title, dataset['title'])

    def test_has_description(self):
        model = self.get_models().first()
        dataset = dataset_from(model)
        assert_equals(model.abstract, dataset['description'])

    def test_has_accrual_periodicity(self):
        model = self.get_models().first()
        dataset = dataset_from(model)
        accrual_periodicity = string_to_accrual_periodicity(model.maintenance_frequency)
        assert_equals(accrual_periodicity, dataset['accrualPeriodicity'])

    def test_has_publisher_name(self):
        model = self.get_models().first()
        dataset = dataset_from(model)
        assert_equals(model.poc.get_full_name(), dataset['publisher']['name'])

    def test_has_publisher_mbox(self):
        model = self.get_models().first()
        dataset = dataset_from(model)
        assert_equals(model.poc.email, dataset['publisher']['mbox'])

    def test_has_distributions(self):
        model = self.get_models().first()
        dataset = dataset_from(model)
        assert_true('distribution' in dataset)

    def test_has_issued(self):
        model = self.get_model()
        dataset = dataset_from(model)
        assert_equals(model.extra_fields.created, dataset['issued'])

    def test_has_no_super_theme(self):
        model = self.get_model()
        dataset = dataset_from(model)
        assert_equals(None, dataset['superTheme'])

    def test_has_super_theme(self):
        model = self.get_AGRI_model()
        dataset = dataset_from(model)
        assert_equals(model.extra_fields.super_theme, dataset['superTheme'])


class DataJsonArDistributionMixin:
    def get_samples(self):
        model = self.get_model()
        return model, LinkFactory.create(resource=model)

    def test_has_access_url(self):
        resource, link = self.get_samples()
        acces_url = get_access_url(resource, link)
        distribution = distribution_from(resource, link)
        assert_equals(acces_url, distribution['accessURL'])

    def test_has_download_url(self):
        resource, link = self.get_samples()
        distribution = distribution_from(resource, link)
        assert_equals(link.url, distribution['downloadURL'])

    def test_has_title(self):
        resource, link = self.get_samples()
        distribution = distribution_from(resource, link)
        assert_equals(link.name, distribution['title'])


class TestDataJsonArDatasetFromDocuments(DataJsonArDatasetMixin,DataJsonArDistributionMixin, TestCase):

    def create_models(self):
        create_models(type='document')

    def get_models(self):
        return Document.objects.all()

class TestDataJsonArDatasetFromLayers(DataJsonArDatasetMixin,DataJsonArDistributionMixin, TestCase):

    def create_models(self):
        create_models(type='layer')

    def get_models(self):
        return Layer.objects.all()
