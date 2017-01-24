from django.shortcuts import render


# Create your views here.

from schapen.models import Schapen
from schapen.forms import AddSchapen
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
import datetime
import forms
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse



# view na login, alles met suffix bedrijf
@login_required
def bedrijf_index(request):
    today = datetime.datetime.today()
    schapen_overzicht = Schapen.objects.filter(Q(einddatum__gt = today) | Q(einddatum__isnull = True )).order_by('intern_nummer')
    context = {'schapen_overzicht':schapen_overzicht}
    return render(request, 'bedrijf/index.html', context)

@login_required
def bedrijf_aanwezige_schapen(request):
    today = datetime.datetime.today()
    schapen_overzicht = Schapen.objects.filter(Q(einddatum__gt = today) | Q(einddatum__isnull = True )).order_by('intern_nummer')
    context = {'schapen_overzicht':schapen_overzicht}
    return render(request, 'bedrijf/aanwezige_schapen.html', context)

@login_required
def bedrijf_alle_schapen(request):
    schapen_overzicht = Schapen.objects.order_by('intern_nummer')
    context = {'schapen_overzicht':schapen_overzicht}
    return render(request, 'bedrijf/alle_schapen.html', context)

@login_required
def bedrijf_schaap_toevoegen(request):
    if request.method == "POST":
        form = AddSchapen(request.POST)
        if form.is_valid():
            formulier = form.save(commit=False)
            formulier.user_name = request.user
            formulier.pub_datum = datetime.datetime.now()
            formulier.save()
            #schapen_overzicht = Schapen.objects.order_by('intern_nummer')
            #context = {'schapen_overzicht':schapen_overzicht}
            #return render(request, 'bedrijf/alle_schapen.html', context)
            return HttpResponseRedirect(reverse('schapen:bedrijf_schaap_toevoegen'))
    else:
        form = AddSchapen()
        return render(request, 'bedrijf/schaap_toevoegen.html',  {'form': form})
