# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geoandino', '0030_auto_20170822_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geoandinotopiccategory',
            name='topic_taxonomy',
            field=models.ForeignKey(related_name='topic_categories_set', on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='geoandino.TopicTaxonomy', null=True),
        ),
    ]
