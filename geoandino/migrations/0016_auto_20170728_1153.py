# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoandino', '0015_auto_20170728_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geoandinotopiccategory',
            name='topic_taxonomy',
            field=models.ForeignKey(related_name='topic_categories_set', to='geoandino.TopicTaxonomy'),
        ),
    ]
