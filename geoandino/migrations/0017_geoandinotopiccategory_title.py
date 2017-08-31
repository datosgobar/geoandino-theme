# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoandino', '0016_auto_20170728_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='geoandinotopiccategory',
            name='title',
            field=models.CharField(default=None, max_length=255, null=True, blank=True),
        ),
    ]
