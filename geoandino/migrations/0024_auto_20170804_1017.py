# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoandino', '0023_auto_20170802_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteconfiguration',
            name='instagram_url',
        ),
        migrations.RemoveField(
            model_name='siteconfiguration',
            name='youtube_url',
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='about_description',
            field=models.TextField(null=True, verbose_name='descripci\xf3n', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='about_title',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='t\xedtulo ', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='facebook_google_description',
            field=models.TextField(null=True, verbose_name='descripci\xf3n', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='facebook_google_title',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='t\xedtulo ', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='twitter_description',
            field=models.TextField(null=True, verbose_name='descripci\xf3n', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='twitter_title',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='t\xedtulo ', blank=True),
        ),
    ]
