# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoandino', '0005_auto_20170720_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfiguration',
            name='document_description',
            field=models.TextField(max_length=250, null=True, verbose_name='Document Description', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='layer_description',
            field=models.TextField(max_length=250, null=True, verbose_name='Layer Description', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='map_description',
            field=models.TextField(max_length=250, null=True, verbose_name='Map Description', blank=True),
        ),
    ]
