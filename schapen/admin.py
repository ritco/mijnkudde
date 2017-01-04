from django.contrib import admin

# Register your models here.

# aanpassing is nodig om de schapen gegevens in de admin backend te zien

from schapen.models import *

class SchapenAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('intern_nummer', 'geslacht', 'geboortedatum','user_name')
    list_filter = ['geslacht']

admin.site.register(Schapen, SchapenAdmin)
