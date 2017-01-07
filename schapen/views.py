from django.shortcuts import render


# Create your views here.

from schapen.models import Schapen
from django.http import HttpResponse



# view na login, alles met suffix bedrijf

def bedrijf_index(request):
    schapen_overzicht = Schapen.objects.all()[:3]
    context = {'schapen_overzicht':schapen_overzicht}
    return render(request, 'bedrijf/index.html', context)
