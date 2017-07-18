# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoandino', '0004_auto_20170718_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfiguration',
            name='about_visible',
            field=models.BooleanField(default=False, verbose_name='Visible'),
        ),
    ]
