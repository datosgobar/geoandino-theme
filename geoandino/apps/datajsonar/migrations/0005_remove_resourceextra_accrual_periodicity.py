# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datajsonar', '0004_resourceextra_accrual_periodicity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resourceextra',
            name='accrual_periodicity',
        ),
    ]
