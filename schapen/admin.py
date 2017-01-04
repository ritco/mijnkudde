from django.contrib import admin

# Register your models here.

# aanpassing is nodig om de schapen gegevens in de admin backend te zien

from .models import Schapen

admin.site.register(Schapen)
