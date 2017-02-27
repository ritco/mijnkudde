
# coding=utf-8

from django.contrib import admin

# Register your models here.

# aanpassing is nodig om de schapen gegevens in de admin backend te zien

from schapen.models import *

class SchapenAdmin(admin.ModelAdmin):
    model = Schapen
    list_display = ('user', 'intern_nummer', 'geslacht', 'geboortedatum', 'einddatum', 'Sanitel','vader','moeder')
    list_filter = ['geslacht', 'user']

admin.site.register(Schapen, SchapenAdmin)
