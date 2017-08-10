# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import exclusivebooleanfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('geoandino', '0010_auto_20170721_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfiguration',
            name='default',
            field=exclusivebooleanfield.fields.ExclusiveBooleanField(default=False),
        ),
    ]
