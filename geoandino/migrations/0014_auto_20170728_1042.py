# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '24_to_26'),
        ('geoandino', '0013_auto_20170728_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeoAndinoTopicCategory',
            fields=[
                ('topiccategory_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='base.TopicCategory')),
            ],
            bases=('base.topiccategory',),
        ),
        migrations.CreateModel(
            name='TopicTaxonomy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identifier', models.CharField(max_length=255)),
                ('limit', models.PositiveIntegerField(default=100)),
                ('offset', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='geoandinotopiccategory',
            name='topic_taxonomy',
            field=models.ForeignKey(to='geoandino.TopicTaxonomy'),
        ),
    ]
