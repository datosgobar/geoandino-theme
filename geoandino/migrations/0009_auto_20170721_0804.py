# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoandino', '0008_auto_20170721_0739'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='logo_footer',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='logo_header',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
