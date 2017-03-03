# coding=utf-8

from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.db.models import Q
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from schapen.middleware.global_request import get_request


class SchapenManager(models.Manager):
    def get_queryset(self):
        request = get_request()
        if request:
            print(request.user)
        if request is not None and not request.user.is_superuser:
            return super(SchapenManager, self)\
                .get_queryset().filter(owner=request.user)
        return super(SchapenManager, self).get_queryset()


class Schapen(models.Model):
    geslacht_keuzes = ((1, 'Ram'), (2, 'Ooi'))
    objects = SchapenManager()

    id = models.AutoField(primary_key=True)
    intern_nummer = models.CharField(max_length=50)
    geslacht = models.IntegerField(choices=geslacht_keuzes)
    geboortedatum = models.DateField(null=True, blank=True)
    einddatum = models.DateField(null=True, blank=True)
    Sanitel = models.CharField(max_length=11)
    moeder = models.ForeignKey('Schapen', models.SET_NULL, null=True,
        related_name='moeders', blank=True
    )
    vater = models.ForeignKey('Schapen', models.SET_NULL, null=True,
        related_name='vaters', blank=True
    )
    owner = models.ForeignKey(User, default=1, null=True)
    pub_datum = models.DateField(null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.__class__.__name__, self.intern_nummer)
