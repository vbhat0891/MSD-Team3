# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-21 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eBedTrack', '0004_auto_20171021_0235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='id',
        ),
        migrations.AddField(
            model_name='hospital',
            name='hospital_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]