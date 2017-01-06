from django.shortcuts import render
from django.template import loader, RequestContext

# Create your views here.

from schapen.models import Schapen
from django.http import HttpResponse

# def schapen_list(request):
#    schapen_list = Schapen.objects.order_by('-intern_nummer')
#    context = {'schapen_list':schapen_list}
#    return render(request, 'schapen/schapen_list.html', context)

def index(request):
    schapen_overzicht = Schapen.objects.all()[:3]

    template = loader.get_template('schapen/index.html')
    context = RequestContext(request, {'schapen_overzicht':schapen_overzicht})

    output = ', '. join (p.intern_nummer for p in schapen_overzicht)
    return HttpResponse(template.render(context))
