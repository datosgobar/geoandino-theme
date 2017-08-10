# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoandino', '0012_auto_20170727_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfiguration',
            name='image_background',
            field=models.ImageField(default=None, null=True, upload_to=b'thumbs/', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='logo_footer',
            field=models.ImageField(null=True, upload_to=b'thumbs/', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='logo_header',
            field=models.ImageField(null=True, upload_to=b'thumbs/', blank=True),
        ),
    ]
