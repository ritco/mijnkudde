from django import forms
from django.forms import extras
from .models import Schapen
from django.forms.fields import DateField
from django.db.models import Q
from django.contrib.auth.models import User

from .middleware.global_request import get_request


class AddSchapen(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AddSchapen, self).__init__( *args, **kwargs)
        user = get_request().user
        self.fields['moeder'].queryset = Schapen.objects.filter(owner=user, geslacht=2)
        self.fields['vader'].queryset = Schapen.objects.filter(owner=user, geslacht=1)

    class Meta:
        model = Schapen
        exclude = ('owner','pub_datum')
