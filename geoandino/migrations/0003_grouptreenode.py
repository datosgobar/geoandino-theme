# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '24_initial'),
        ('geoandino', '0002_auto_20170907_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupTreeNode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('children_nodes', models.ForeignKey(related_name='children', to='geoandino.GroupTreeNode', null=True)),
                ('group', models.OneToOneField(to='groups.GroupProfile')),
                ('parent', models.OneToOneField(null=True, default=None, to='geoandino.GroupTreeNode')),
            ],
            options={
                'ordering': ['group__title'],
            },
        ),
    ]
