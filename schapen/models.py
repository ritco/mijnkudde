
# coding=utf-8

from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.db.models import Q
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

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
        limit_choices_to = {'geslacht': 2},
        )
    vader = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name = 'ram_lam',
        limit_choices_to={'geslacht': 1},
        )
    owner = models.ForeignKey(User, default=1, null=True)
    pub_datum = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return self.intern_nummer

class CustomModelForm(forms.ModelForm):
    """
    Sandboxes user data for each reference field pointing to an
    object with an "owner" field.
    """
    def __init__(self, request, *args, **kwargs):
        # cache the request object
        self.request = request
        init_result = super(CustomModelForm, self).__init__(*args, **kwargs)

        # go through each field in this ModelForm
        for field_name, field_widget in self.fields.iteritems():
            # find the model field definition
            model_field = getattr(self.Meta.model, field_name, None)
            if model_field:
                # check if it has a related model
                related_model = getattr(model_field.field, 'related_model', None)
                if related_model:
                    # check if it has an owner field
                    owner_field = getattr(related_model, 'owner', None)
                    if owner_field:
                        # filter field objects by owner = logged in user
                        field_widget.queryset = related_model.objects.filter(owner=request.user)

        return init_result
