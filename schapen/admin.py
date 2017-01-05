from django.contrib import admin

# Register your models here.

# aanpassing is nodig om de schapen gegevens in de admin backend te zien

from Schapen.models import *

admin.site.register(schapen)
