# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoandino', '0020_remove_geoandinotopiccategory_title'),
    ]

    operations = [
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
    ]
