# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '24_initial'),
        ('geoandino', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupTreeNode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('children_nodes', models.ForeignKey(related_name='children', to='geoandino.GroupTreeNode', null=True)),
                ('group', models.OneToOneField(to='groups.GroupProfile')),
            ],
            options={
                'ordering': ['group__title'],
            },
        ),
    ]
