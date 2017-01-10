from django import forms

from .models import Schapen

class AddSchapen(forms.ModelForm):

    class Meta:
        model = Schapen
        fields = ('intern_nummer', 'geslacht', 'geboortedatum', 'Sanitel', 'moeder', 'vader')
