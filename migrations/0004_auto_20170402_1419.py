# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BillSplitter', '0003_bill_amount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bill',
            options={'ordering': ['-created_date']},
        ),
        migrations.AlterField(
            model_name='bill',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
