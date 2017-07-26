# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoandino', '0002_siteconfiguration_default'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='siteconfiguration',
            options={'ordering': ['created']},
        ),
    ]
