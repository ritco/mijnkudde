from django import forms
from django.forms import extras
from .models import Schapen
from django.forms.fields import DateField


class AddSchapen(forms.ModelForm):




    class Meta:
        model = Schapen
        exclude = ('user_name', )
