# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoandino', '0004_auto_20170720_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='document_description',
            field=models.CharField(default=b'', max_length=250, verbose_name='Document Description'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='layer_description',
            field=models.CharField(default=b'', max_length=250, verbose_name='Layer Description'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='map_description',
            field=models.CharField(default=b'', max_length=250, verbose_name='Map Description'),
        ),
    ]
