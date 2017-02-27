from django import forms
from django.forms import extras
from .models import Schapen
from django.forms.fields import DateField
from django.db.models import Q
from django.contrib.auth.models import User


class AddSchapen(forms.Form):

    def __init__(self, *args, **kwargs):
          super(AddSchapen, self).__init__(*args, **kwargs)
          gebruiker = request.user
          self.fields['moeder'] = forms.ChoiceField(choices=[ (o.id, str(o)) for o in Schapen.objects.filter(owner=gebruiker).filter(geslacht=2)])
          self.fields['vader'] = forms.ChoiceField(choices=[ (o.id, str(o)) for o in Schapen.objects.filter(owner=gebruiker).filter(geslacht=1)])

    class Meta:
        model = Schapen
        exclude = ('owner', )
