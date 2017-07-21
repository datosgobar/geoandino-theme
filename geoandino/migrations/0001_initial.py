# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20160822_0917'),
        ('base', '24_to_26'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceExtra',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('resource', models.OneToOneField(related_name='extra_fields', primary_key=True, serialize=False, to='base.ResourceBase')),
                ('super_theme', models.CharField(blank=True, max_length=10, null=True, choices=[(b'agri', b'Agroganader\xc3\xada, pesca y forestaci\xc3\xb3n'), (b'econ', b'Econom\xc3\xada y finanzas'), (b'educ', b'Educaci\xc3\xb3n, cultura y deportes'), (b'ener', b'Energ\xc3\xada'), (b'envi', b'Medio ambiente'), (b'gove', b'Gobierno y sector p\xc3\xbablico'), (b'heal', b'Salud'), (b'intr', b'Asuntos internacionales'), (b'just', b'Justicia, seguridad y legales'), (b'regi', b'Regiones y ciudades'), (b'soci', b'Poblaci\xc3\xb3n y sociedad'), (b'tech', b'Ciencia y tecnolog\xc3\xada'), (b'tran', b'Transporte')])),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('default', models.BooleanField(default=False)),
                ('publisher', models.ForeignKey(to='account.EmailAddress')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
