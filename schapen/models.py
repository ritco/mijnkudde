from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Schapen(models.Model):
    geslacht_keuzes = ((1, 'Ram'), (2, 'Ooi'))

    intern_nummer = models.CharField(max_length=50)
    geslacht = models.IntegerField(choices=geslacht_keuzes)
    geboortedatum = models.DateTimeField()
    einddatum = models.DateTimeField()
    Sanitel = models.CharField(max_length=11)