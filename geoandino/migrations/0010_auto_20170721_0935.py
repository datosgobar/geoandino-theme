# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoandino', '0009_auto_20170721_0804'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='group_description',
            field=models.TextField(max_length=250, null=True, verbose_name='Group description', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='group_visible',
            field=models.BooleanField(default=False, verbose_name='Visible'),
        ),
    ]
