# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoandino', '0003_auto_20170713_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='about_description',
            field=models.TextField(null=True, verbose_name='description', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='about_title',
            field=models.CharField(default='', max_length=255, verbose_name='title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='about_visible',
            field=models.BooleanField(default=False),
        ),
    ]
