# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('BillSplitter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner', models.IntegerField()),
                ('debtor_id', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('paid', models.BooleanField()),
                ('paid_date', models.DateTimeField(null=True, blank=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
