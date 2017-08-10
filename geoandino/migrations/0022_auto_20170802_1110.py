# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoandino', '0021_auto_20170802_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geoandinotopiccategory',
            name='topic_taxonomy',
            field=models.ForeignKey(related_name='topic_categories_set', default=None, to='geoandino.TopicTaxonomy', null=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='about_description',
            field=models.TextField(null=True, verbose_name='description', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='about_title',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='title', blank=True),
        ),
    ]
