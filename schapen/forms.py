from django import forms
from django.forms import extras
from .models import Schapen


class AddSchapen(forms.ModelForm):

    class Meta:
        model = Schapen
        fields = ('intern_nummer', 'geslacht', 'geboortedatum', 'Sanitel', 'moeder', 'vader')
        widgets = {
            'geboortedatum': forms.DateField(format='%d/%m/%Y'),         
        }
