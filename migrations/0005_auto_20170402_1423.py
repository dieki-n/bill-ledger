# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BillSplitter', '0004_auto_20170402_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='amount',
            field=models.DecimalField(default=0, max_digits=7, decimal_places=2),
        ),
    ]
