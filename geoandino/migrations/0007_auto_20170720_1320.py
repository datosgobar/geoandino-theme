# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoandino', '0006_auto_20170720_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='icon_display',
            field=models.BooleanField(default=False, verbose_name='Icon display'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='contact_mail',
            field=models.CharField(default=b'contact@portal.com', max_length=250, verbose_name='Contact mail'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='document_description',
            field=models.TextField(max_length=250, null=True, verbose_name='Document description', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='layer_description',
            field=models.TextField(max_length=250, null=True, verbose_name='Layer description', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='map_description',
            field=models.TextField(max_length=250, null=True, verbose_name='Map description', blank=True),
        ),
    ]
