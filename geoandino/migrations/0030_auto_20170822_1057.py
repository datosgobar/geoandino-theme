# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoandino', '0029_topictaxonomy_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfiguration',
            name='facebook_google_description',
            field=models.TextField(null=True, verbose_name='Facebook and Google description', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='facebook_google_image',
            field=models.ImageField(upload_to=b'thumbs/', null=True, verbose_name='Facebook and Google image', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='facebook_google_title',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='Facebook and Google title', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='twitter_description',
            field=models.TextField(null=True, verbose_name='Twitter description', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='twitter_image',
            field=models.ImageField(upload_to=b'thumbs/', null=True, verbose_name='Twitter image', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='twitter_title',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='Twitter title', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='twitter_user',
            field=models.CharField(max_length=100, null=True, verbose_name='Twitter user', blank=True),
        ),
    ]
