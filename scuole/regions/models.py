# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from scuole.states.models import State
from scuole.stats.models import SchoolYear, StatsBase
from scuole.cohorts.models import CohortYear, CohortBase
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Region(models.Model):
    name = models.CharField(_('Geographic name for region'), max_length=20)
    region_id = models.CharField(_('Region identifier'), max_length=2)
    slug = models.SlugField()
    state = models.ForeignKey(State, related_name='regions')

    def __str__(self):
        return '{} - {}'.format(self.name, self.region_id)


@python_2_unicode_compatible
class RegionStats(StatsBase):
    region = models.ForeignKey(Region, related_name='stats')
    year = models.ForeignKey(SchoolYear, related_name='region_stats')

    class Meta:
        unique_together = ('region', 'year',)
        verbose_name_plural = _('Region stats')

    def __str__(self):
        return '{0} {1}'.format(self.year.name, self.region.name)


@python_2_unicode_compatible
class RegionCohort(CohortBase):
    region_cohort = models.ForeignKey(Region, related_name='cohort')
    cohort_year = models.ForeignKey(CohortYear, related_name='region_cohort')

    class Meta:
        unique_together = ('region_cohort', 'cohort_year',)
        verbose_name_plural = _('Region cohort')

    def __str__(self):
        return '{0} {1}'.format(self.cohort_year.name, self.region_cohort.name)
