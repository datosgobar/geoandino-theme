# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoandino', '0027_auto_20170815_1438'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topictaxonomy',
            options={'ordering': ['identifier']},
        ),
    ]
