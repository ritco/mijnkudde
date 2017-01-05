from django.shortcuts import render

# Create your views here.

from .models import Schapen

def schapen_list(request):
    schapen_list = Schapen.objects.order_by('-intern_nummer')
    context = {'schapen_list':schapen_list}
    return render(request, 'schapen/schapen_list.html', context)
