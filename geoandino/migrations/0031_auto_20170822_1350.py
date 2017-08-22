# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoandino', '0030_auto_20170822_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfiguration',
            name='contact_mail',
            field=models.CharField(default=b'contact@portal.com', max_length=250, null=True, verbose_name='Email de contacto', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='document_description',
            field=models.TextField(max_length=250, null=True, verbose_name='Descripci\xf3n de documentos', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='facebook_google_description',
            field=models.TextField(null=True, verbose_name='Descripci\xf3n de Facebook y Google', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='facebook_google_image',
            field=models.ImageField(upload_to=b'thumbs/', null=True, verbose_name='Imagen de Facebook y Google', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='facebook_google_title',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='T\xedtulo de Facebook y Google', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='group_description',
            field=models.TextField(max_length=250, null=True, verbose_name='Descripci\xf3n de grupos', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='icon_display',
            field=models.BooleanField(default=False, verbose_name='Mostrar \xedconos de categor\xedas'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='image_background',
            field=models.ImageField(default=None, upload_to=b'thumbs/', null=True, verbose_name='Image background', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='layer_description',
            field=models.TextField(max_length=250, null=True, verbose_name='Descripci\xf3n de capas', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='logo_footer',
            field=models.ImageField(upload_to=b'thumbs/', null=True, verbose_name='Logo footer', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='logo_header',
            field=models.ImageField(upload_to=b'thumbs/', null=True, verbose_name='Logo header', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='map_description',
            field=models.TextField(max_length=250, null=True, verbose_name='Descripci\xf3n de mapas', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='site_url',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='URL del sitio', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='twitter_description',
            field=models.TextField(null=True, verbose_name='Descripci\xf3n de Twitter', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='twitter_image',
            field=models.ImageField(upload_to=b'thumbs/', null=True, verbose_name='Imagen de Twitter', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='twitter_title',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='T\xedtulo de Twitter', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='twitter_user',
            field=models.CharField(max_length=100, null=True, verbose_name='Usuario de Twitter', blank=True),
        ),
    ]
