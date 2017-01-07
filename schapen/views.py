from django.shortcuts import render


# Create your views here.

from schapen.models import Schapen, Q
from django.http import HttpResponse



# view na login, alles met suffix bedrijf

def bedrijf_index(request):
    today = datetime.datetime.today()
    schapen_overzicht = Schapen.objects.filter(Q(einddatum=today)|Q(einddatum=None))
    context = {'schapen_overzicht':schapen_overzicht}
    return render(request, 'bedrijf/index.html', context)
