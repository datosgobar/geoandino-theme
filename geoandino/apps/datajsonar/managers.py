# -*- coding: utf-8 -*-
from django.db import models

class ResourceExtraManager(models.Manager):

    def create_for(self, resource):
        return self.create(resource=resource)

    def touch(self, resource):
        self.get(resource=resource).save()

class LinkExtraManager(models.Manager):

    def create_for(self, link):
        return self.create(link=link)
