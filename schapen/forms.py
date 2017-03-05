from django import forms
from django.forms import extras
from .models import Schapen
from django.forms.fields import DateField
from django.db.models import Q
from django.contrib.auth.models import User



class AddSchapen(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
          super(AddSchapen, self).__init__( *args, **kwargs)
          self.fields['moeder'] = forms.ChoiceField(
          choices=[(o.id, str(o)) for o in Schapen.objects.filter(owner=user).filter(geslacht=2)],
          required=False
          )
          self.fields['vader'] = forms.ChoiceField(
          choices=[(o.id, str(o)) for o in Schapen.objects.filter(owner=user).filter(geslacht=1)],
          required=False
          )

    class Meta:
        model = Schapen
        exclude = ('owner','pub_datum')
