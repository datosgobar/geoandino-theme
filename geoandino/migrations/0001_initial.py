# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields
import exclusivebooleanfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_signupcode_username'),
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
            name='SiteConfiguration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('default', exclusivebooleanfield.fields.ExclusiveBooleanField(default=False)),
                ('about_visible', models.BooleanField(default=False, verbose_name='Visible')),
                ('about_title', models.CharField(default=None, max_length=255, null=True, verbose_name='t\xedtulo ', blank=True)),
                ('about_description', models.TextField(null=True, verbose_name='descripci\xf3n', blank=True)),
                ('image_background', models.ImageField(default=None, null=True, upload_to=b'thumbs/', blank=True)),
                ('facebook_url', models.CharField(default=b'http://www.facebook.com/portal', max_length=150, null=True, verbose_name='Facebook', blank=True)),
                ('twitter_url', models.CharField(default=b'http://www.twitter.com/portal', max_length=150, null=True, verbose_name='Twitter', blank=True)),
                ('github_url', models.CharField(default=b'http://www.github.com/portal', max_length=150, null=True, verbose_name='GitHub', blank=True)),
                ('contact_mail', models.CharField(default=b'contact@portal.com', max_length=250, null=True, verbose_name='Contact mail', blank=True)),
                ('layer_description', models.TextField(max_length=250, null=True, verbose_name='Layer description', blank=True)),
                ('map_description', models.TextField(max_length=250, null=True, verbose_name='Map description', blank=True)),
                ('document_description', models.TextField(max_length=250, null=True, verbose_name='Document description', blank=True)),
                ('group_description', models.TextField(max_length=250, null=True, verbose_name='Group description', blank=True)),
                ('group_visible', models.BooleanField(default=False, verbose_name='Visible')),
                ('icon_display', models.BooleanField(default=False, verbose_name='Icon display')),
                ('site_url', models.CharField(default=None, max_length=255, null=True, verbose_name='Site url', blank=True)),
                ('logo_footer', models.ImageField(null=True, upload_to=b'thumbs/', blank=True)),
                ('logo_header', models.ImageField(null=True, upload_to=b'thumbs/', blank=True)),
                ('facebook_google_image', models.ImageField(upload_to=b'thumbs/', null=True, verbose_name='Facebook and Google image', blank=True)),
                ('facebook_google_title', models.CharField(default=None, max_length=255, null=True, verbose_name='Facebook and Google title', blank=True)),
                ('facebook_google_description', models.TextField(null=True, verbose_name='Facebook and Google description', blank=True)),
                ('twitter_image', models.ImageField(upload_to=b'thumbs/', null=True, verbose_name='Twitter image', blank=True)),
                ('twitter_title', models.CharField(default=None, max_length=255, null=True, verbose_name='Twitter title', blank=True)),
                ('twitter_description', models.TextField(null=True, verbose_name='Twitter description', blank=True)),
                ('twitter_user', models.CharField(max_length=100, null=True, verbose_name='Twitter user', blank=True)),
                ('publisher', models.ForeignKey(to='account.EmailAddress')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='TopicTaxonomy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identifier', models.CharField(max_length=255)),
                ('description', models.CharField(default=None, max_length=255, null=True, blank=True)),
                ('limit', models.PositiveIntegerField(default=100)),
                ('offset', models.IntegerField(default=0)),
                ('image', models.ImageField(null=True, upload_to=b'thumbs/', blank=True)),
                ('icon', models.CharField(default=None, max_length=20, null=True, blank=True)),
            ],
            options={
                'ordering': ['identifier'],
            },
        ),
        migrations.AddField(
            model_name='geoandinotopiccategory',
            name='topic_taxonomy',
            field=models.ForeignKey(related_name='topic_categories_set', default=None, blank=True, to='geoandino.TopicTaxonomy', null=True),
        ),
    ]
