# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BillSplitter', '0002_auto_20170329_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='amount',
            field=models.FloatField(default=0),
        ),
    ]
