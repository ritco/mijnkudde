from django.shortcuts import render


# Create your views here.

from schapen.models import Schapen
from schapen.forms import AddSchapen
from django.db.models import Q
from django.http import HttpResponse
import datetime
import forms



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
    return render(request, 'bedrijf/alle_schapen.html', context)

def bedrijf_schaap_toevoegen(request):
    if request.method == "POST":
        form = AddSchapen(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bedrijf_alle_schapen')
    else:
        form = AddSchapen()
    return render(request, 'bedrijf/schaap_toevoegen.html',  {'form': form})
