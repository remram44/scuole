# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('districts', '0014_districtstats_teacher_base_salary_average'),
    ]

    operations = [
        migrations.AlterField(
            model_name='districtstats',
            name='teacher_base_salary_average',
            field=models.DecimalField(blank=True, max_digits=10, decimal_places=2, verbose_name='Average teacher salary at entity', null=True),
        ),
    ]
