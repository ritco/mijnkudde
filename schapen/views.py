from django.shortcuts import render


# Create your views here.

from schapen.models import Schapen
from django.db.models import Q
from django.http import HttpResponse
import datetime



# view na login, alles met suffix bedrijf

def bedrijf_index(request):
    today = datetime.datetime.today()
    schapen_overzicht = Schapen.objects.filter(Q(einddatum__gt = today) | Q(einddatum__isnull = True )).order_by('intern_nummer')
    context = {'schapen_overzicht':schapen_overzicht}
    return render(request, 'bedrijf/index.html', context)


def bedrijf_aanwezige_schapen(request):
    today = datetime.datetime.today()
    schapen_overzicht = Schapen.objects.filter(Q(einddatum__gt = today) | Q(einddatum__isnull = True )).order_by('intern_nummer')
    context = {'schapen_overzicht':schapen_overzicht}
    return render(request, 'bedrijf/aanwezige_schapen.html', context)

def bedrijf_alle_schapen(request):
    schapen_overzicht = Schapen.objects.order_by('intern_nummer')
    context = {'schapen_overzicht':schapen_overzicht}
    return render(request, 'bedrijf/aanwezige_schapen.html', context)
