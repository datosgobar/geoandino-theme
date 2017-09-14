# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datajsonar', '0003_auto_20170802_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourceextra',
            name='accrual_periodicity',
            field=models.CharField(default=b'R/PT1S', max_length=10, choices=[(b'R/P10Y', 'decennial'), (b'R/P4Y', 'quadrennial'), (b'R/P1Y', 'annual'), (b'R/P2M', 'bimonthly'), (b'R/P3.5D', 'semiweekly'), (b'R/P1D', 'daily'), (b'R/P2W', 'biweekly'), (b'R/P6M', 'semiannual'), (b'R/P2Y', 'biennial'), (b'R/P3Y', 'triennial'), (b'R/P0.33W', 'three times a week'), (b'R/P0.33M', 'three times a month'), (b'R/PT1S', 'continuously updated'), (b'R/P1M', 'monthly'), (b'R/P3M', 'quarterly'), (b'R/P0.5M', 'semimonthly'), (b'R/P4M', 'three times a year'), (b'R/P1W', 'weekly'), (b'R/PT1H', 'hourly')]),
        ),
    ]
