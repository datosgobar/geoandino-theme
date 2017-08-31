# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoandino', '0028_auto_20170815_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='topictaxonomy',
            name='icon',
            field=models.CharField(default=None, max_length=20, null=True, blank=True),
        ),
    ]
