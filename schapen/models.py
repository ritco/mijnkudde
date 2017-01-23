
# coding=utf-8

from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from django.utils.encoding import python_2_unicode_compatible

# Create your models here.


class Schapen(models.Model):
    geslacht_keuzes = ((1, 'Ram'), (2, 'Ooi'))

    id = models.AutoField(primary_key=True)
    intern_nummer = models.CharField(max_length=50)
    geslacht = models.IntegerField(choices=geslacht_keuzes)
    geboortedatum = models.DateField(null=True, blank=True)
    einddatum = models.DateField(null=True, blank=True)
    Sanitel = models.CharField(max_length=11)
    moeder = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name = 'ooi_lam',
        limit_choices_to={'geslacht': 2},
        )
    vader = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name = 'ram_lam',
        limit_choices_to={'geslacht': 1},
        )
    user_name = models.CharField(max_length=100, null=True, blank=True)
    pub_datum = models.DateField(null=True, blank=True)



    def __unicode__(self):
        return self.intern_nummer
