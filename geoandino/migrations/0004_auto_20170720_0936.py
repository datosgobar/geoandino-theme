# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoandino', '0003_auto_20170713_0928'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookAndGoogleMetadata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TwitterMetadata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'')),
                ('tw_user', models.CharField(max_length=100, verbose_name='Twitter User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='about_description',
            field=models.TextField(null=True, verbose_name='description', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='about_title',
            field=models.CharField(default=None, max_length=255, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='about_visible',
            field=models.BooleanField(default=False, verbose_name='Visible'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='contact_mail',
            field=models.CharField(default=b'contact@portal.com', max_length=250, verbose_name='Contact Mail'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='facebook_url',
            field=models.CharField(default=b'www.facebook.com/portal', max_length=150, verbose_name='Facebook'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='github_url',
            field=models.CharField(default=b'www.github.com/portal', max_length=150, verbose_name='GitHub'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='image_background',
            field=models.ImageField(null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='instagram_url',
            field=models.CharField(default=b'www.instagram.com/portal', max_length=150, verbose_name='Instagram'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='twitter_url',
            field=models.CharField(default=b'www.twitter.com/portal', max_length=150, verbose_name='Twitter'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='youtube_url',
            field=models.CharField(default=b'www.youtube.com/portal', max_length=150, verbose_name='Youtube'),
        ),
        migrations.AddField(
            model_name='twittermetadata',
            name='site_configuration',
            field=models.ForeignKey(to='geoandino.SiteConfiguration'),
        ),
        migrations.AddField(
            model_name='facebookandgooglemetadata',
            name='site_configuration',
            field=models.ForeignKey(to='geoandino.SiteConfiguration'),
        ),
    ]
