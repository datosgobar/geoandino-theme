# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '24_to_26'),
        ('geoandino', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceExtra',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('resource', models.OneToOneField(related_name='extra_fields', primary_key=True, serialize=False, to='base.ResourceBase')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
    ]
