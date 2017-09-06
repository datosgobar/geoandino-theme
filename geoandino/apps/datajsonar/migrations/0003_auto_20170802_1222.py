# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import geoandino.apps.datajsonar.models


class Migration(migrations.Migration):

    dependencies = [
        ('datajsonar', '0002_linkextra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourceextra',
            name='super_theme',
            field=models.CharField(default=geoandino.apps.datajsonar.models.get_default_super_theme, max_length=10, choices=[(b'agri', b'Agroganader\xc3\xada, pesca y forestaci\xc3\xb3n'), (b'econ', b'Econom\xc3\xada y finanzas'), (b'educ', b'Educaci\xc3\xb3n, cultura y deportes'), (b'ener', b'Energ\xc3\xada'), (b'envi', b'Medio ambiente'), (b'gove', b'Gobierno y sector p\xc3\xbablico'), (b'heal', b'Salud'), (b'intr', b'Asuntos internacionales'), (b'just', b'Justicia, seguridad y legales'), (b'regi', b'Regiones y ciudades'), (b'soci', b'Poblaci\xc3\xb3n y sociedad'), (b'tech', b'Ciencia y tecnolog\xc3\xada'), (b'tran', b'Transporte')]),
        ),
    ]
