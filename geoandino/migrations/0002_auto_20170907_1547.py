# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('geoandino', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfiguration',
            name='about_description',
            field=ckeditor.fields.RichTextField(default=None, null=True, verbose_name='descripci\xf3n'),
        ),
    ]
