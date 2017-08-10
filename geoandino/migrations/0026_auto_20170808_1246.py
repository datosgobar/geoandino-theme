# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoandino', '0025_auto_20170804_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfiguration',
            name='facebook_url',
            field=models.CharField(default=b'http://www.facebook.com/portal', max_length=150, null=True, verbose_name='Facebook', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='github_url',
            field=models.CharField(default=b'http://www.github.com/portal', max_length=150, null=True, verbose_name='GitHub', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='twitter_url',
            field=models.CharField(default=b'http://www.twitter.com/portal', max_length=150, null=True, verbose_name='Twitter', blank=True),
        ),
    ]
