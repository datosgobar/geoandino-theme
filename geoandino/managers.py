# -*- coding: utf-8 -*-
from django.db import models

class ResourceExtraManager(models.Manager):

    def create_for(self, resource):
        return self.create(resource=resource)
