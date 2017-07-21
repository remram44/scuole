# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-19 19:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cohorts', '0001_initial'),
        ('states', '0004_auto_20170216_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='StateCohort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ethnicity', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=15)),
                ('economic_status', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
                ('enrolled_8th', models.IntegerField()),
                ('enrolled_9th', models.IntegerField()),
                ('enrolled_9th_percent', models.FloatField()),
                ('enrolled_10th', models.IntegerField()),
                ('enrolled_10th_percent', models.FloatField()),
                ('lessthan_10th_enrolled', models.IntegerField()),
                ('lessthan_10th_enrolled_percent', models.FloatField()),
                ('graduated', models.IntegerField()),
                ('graduated_percent', models.FloatField()),
                ('enrolled_4yr', models.IntegerField()),
                ('enrolled_4yr_percent', models.FloatField()),
                ('enrolled_2yr', models.IntegerField()),
                ('enrolled_2yr_percent', models.FloatField()),
                ('total_enrolled', models.IntegerField()),
                ('total_enrolled_percent', models.FloatField()),
                ('total_degrees', models.IntegerField()),
                ('total_degrees_percent', models.FloatField()),
                ('bacc', models.IntegerField()),
                ('bacc_acc', models.IntegerField()),
                ('bacc_cert', models.IntegerField()),
                ('assoc', models.IntegerField()),
                ('accoc_cert', models.IntegerField()),
                ('cert', models.IntegerField()),
                ('cohort_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state_cohort', to='cohorts.CohortsYear')),
                ('state_cohort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cohort', to='states.State')),
            ],
            options={
                'verbose_name_plural': 'State cohort',
            },
        ),
        migrations.AlterUniqueTogether(
            name='statecohort',
            unique_together=set([('state_cohort', 'cohort_year')]),
        ),
    ]
