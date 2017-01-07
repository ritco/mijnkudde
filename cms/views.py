from django.shortcuts import render

# Create your views here.

# aan te passen from cms.models import Schapen
from django.http import HttpResponse

# view voor basis pagina website, login vetrekt van hier
def index(request):
    return render(request, 'index.html')
