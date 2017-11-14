# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-13 20:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eBedTrack', '0003_contactus_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='ph',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hosp', to='eBedTrack.Hospital'),
        ),
        migrations.AlterField(
            model_name='bed',
            name='bed_type',
            field=models.CharField(choices=[('ICU/CC', 'ICU/CC'), ('EU', 'EU'), ('MED/SURG', 'MED/SURG'), ('OB', 'OB'), ('SICU', 'SICU'), ('Neg-Pres/Iso', 'Neg-Pres/Iso'), ('OR', 'OR'), ('Peds', 'Peds'), ('PICU', 'PICU'), ('NICU', 'NICU'), ('Burn', 'Burn'), ('Mental-Health', 'Mental-Health'), ('Other', 'Other')], default='ICU', max_length=10),
        ),
        migrations.AlterField(
            model_name='patient',
            name='bed_type',
            field=models.CharField(choices=[('ICU/CC', 'ICU/CC'), ('EU', 'EU'), ('MED/SURG', 'MED/SURG'), ('OB', 'OB'), ('SICU', 'SICU'), ('Neg-Pres/Iso', 'Neg-Pres/Iso'), ('OR', 'OR'), ('Peds', 'Peds'), ('PICU', 'PICU'), ('NICU', 'NICU'), ('Burn', 'Burn'), ('Mental-Health', 'Mental-Health'), ('Other', 'Other')], default='ICU ', max_length=10),
        ),
    ]
