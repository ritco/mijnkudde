
# coding=utf-8

from django.contrib import admin

# Register your models here.

# aanpassing is nodig om de schapen gegevens in de admin backend te zien

from schapen.models import *

admin.site.register(Schapen)
