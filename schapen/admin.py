from django.contrib import admin

# Register your models here.

# aanpassing is nodig om de schapen gegevens in de admin backend te zien

from .models import Schapen

class SchapenAdmin(admin.ModelAdmin):
    model = review
    list_display = ('intern_nummer', 'geslacht')

admin.site.register(Schapen, SchapenAdmin)
