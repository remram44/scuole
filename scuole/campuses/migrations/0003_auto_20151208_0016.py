# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-08 00:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('campuses', '0002_campus_county'),
        ('districts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campus',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='campuses', to='districts.District'),
        ),
        migrations.AlterUniqueTogether(
            name='campusstats',
            unique_together=set([('campus', 'year')]),
        ),
    ]
