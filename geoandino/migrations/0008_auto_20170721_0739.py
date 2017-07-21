# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoandino', '0007_auto_20170720_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='site_url',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='Site url', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='about_title',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='title', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='image_background',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
