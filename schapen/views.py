from django.shortcuts import render

# Create your views here.

from schapen.models import Schapen
from django.http import HttpResponse

# def schapen_list(request):
#    schapen_list = Schapen.objects.order_by('-intern_nummer')
#    context = {'schapen_list':schapen_list}
#    return render(request, 'schapen/schapen_list.html', context)

def index(request):
    schapen_overzicht = Schapen.objects.all()[:3]
    output = ', '. join (p.intern_nummer for p in schapen_overzicht)
    return HttpResponse(output)
