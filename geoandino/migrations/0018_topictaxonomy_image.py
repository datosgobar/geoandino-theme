# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoandino', '0017_geoandinotopiccategory_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='topictaxonomy',
            name='image',
            field=models.ImageField(null=True, upload_to=b'thumbs/', blank=True),
        ),
    ]
