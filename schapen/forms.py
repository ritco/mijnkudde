from django import forms

from .models import Schapen
from Schapen import models as m

class AddSchapen(forms.ModelForm):

    class Meta:
        model = m.Schapen
        # fields = ('intern_nummer', 'geslacht', 'geboortedatum', 'Sanitel', 'moeder', 'vader')
