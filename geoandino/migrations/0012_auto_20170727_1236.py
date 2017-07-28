# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoandino', '0011_auto_20170721_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfiguration',
            name='image_background',
            field=models.ImageField(default=None, null=True, upload_to=b'bg/', blank=True),
        ),
    ]
