# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoandino', '0022_auto_20170802_1110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facebookandgooglemetadata',
            name='site_configuration',
        ),
        migrations.RemoveField(
            model_name='twittermetadata',
            name='site_configuration',
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='facebook_google_description',
            field=models.TextField(null=True, verbose_name='description', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='facebook_google_image',
            field=models.ImageField(null=True, upload_to=b'thumbs/', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='facebook_google_title',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='title', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='twitter_description',
            field=models.TextField(null=True, verbose_name='description', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='twitter_image',
            field=models.ImageField(null=True, upload_to=b'thumbs/', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='twitter_title',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='title', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='twitter_user',
            field=models.CharField(max_length=100, null=True, verbose_name='Twitter User', blank=True),
        ),
        migrations.DeleteModel(
            name='FacebookAndGoogleMetadata',
        ),
        migrations.DeleteModel(
            name='TwitterMetadata',
        ),
    ]
