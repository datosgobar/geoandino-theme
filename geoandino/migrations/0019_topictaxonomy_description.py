# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoandino', '0018_topictaxonomy_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='topictaxonomy',
            name='description',
            field=models.CharField(default=None, max_length=255, null=True, blank=True),
        ),
    ]
