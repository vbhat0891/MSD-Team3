# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-21 21:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eBedTrack', '0009_auto_20171021_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='bed_id',
            field=models.CharField(default=501, max_length=20),
        ),
    ]
