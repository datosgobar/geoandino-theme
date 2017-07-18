# -*- coding: utf-8 -*-
from nose.tools import istest, assert_true, assert_equals
from django.test import TestCase
from django.conf import settings
from geonode.base.populate_test_data import create_models
from geonode.layers.models import Layer
from geonode.maps.models import Map
from geonode.documents.models import Document
from geoandino.utils.datajsonar import data_jsonar, dataset_from
from geoandino.tests.test_utils.factories import SiteConfigurationFactory, TopicCategoryFactory


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
        datasets = data_jsonar()['datasets']
        assert_equals([], datasets)

    @istest
    def dataset_from_layers(self):
        create_models(type='layer')

        datasets = data_jsonar()['datasets']
        assert_equals(Layer.objects.count(), len(datasets))

    @istest
    def dataset_from_layers_and_maps(self):
        create_models(type='layer')
        create_models(type='map')
        expected_count = Layer.objects.count() + Map.objects.count()
        datasets = data_jsonar()['datasets']
        assert_equals(expected_count, len(datasets))

    @istest
    def dataset_from_layers__maps_and_documents(self):
        create_models(type='layer')
        create_models(type='map')
        create_models(type='document')
        expected_count = Layer.objects.count() + Map.objects.count() + Document.objects.count()
        datasets = data_jsonar()['datasets']
        assert_equals(expected_count, len(datasets))


class DataJsonArDatasetMixin:

    # Required by create_models() function, from geonode's initial_data.json
    fixtures = ['initial_data.json']

    def setUp(self):
        self.site_conf = SiteConfigurationFactory.create(default=True)
        self.settings = settings
        self.create_models()
        self.expect_keys = ['title', ]

    def create_models(self):
        raise NotImplementedError("This should be implement in a subclass.")

    def get_models(self):
        raise NotImplementedError("This should be implement in a subclass.")

    def test_has_title(self):
        model = self.get_models().first()
        dataset = dataset_from(model)
        assert_equals(model.title, dataset['title'])

    def test_has_description(self):
        model = self.get_models().first()
        dataset = dataset_from(model)
        assert_equals(model.abstract, dataset['description'])

class TestDataJsonArDatasetFromDocuments(DataJsonArDatasetMixin,TestCase):

    def create_models(self):
        create_models(type='document')

    def get_models(self):
        return Document.objects.all()

class TestDataJsonArDatasetFromLayers(DataJsonArDatasetMixin,TestCase):

    def create_models(self):
        create_models(type='layer')

    def get_models(self):
        return Layer.objects.all()

class TestDataJsonArDatasetFromMaps(DataJsonArDatasetMixin,TestCase):

    def create_models(self):
        create_models(type='map')

    def get_models(self):
        return Map.objects.all()