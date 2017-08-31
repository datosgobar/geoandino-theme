# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoandino', '0019_topictaxonomy_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geoandinotopiccategory',
            name='title',
        ),
    ]
