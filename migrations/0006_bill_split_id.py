# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BillSplitter', '0005_auto_20170402_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='split_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
