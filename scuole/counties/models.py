from __future__ import unicode_literals\

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class County(models.Model):
    name = models.CharField(help_text="County name", max_length=100)
    slug = models.SlugField()
    fips = models.IntegerField(help_text="County fips code")

    def __str__(self):
        return self.name
