from django.contrib import admin

# Register your models here.

# aanpassing is nodig om de schapen gegevens in de admin backend te zien

from django.db.models import get_models, get_app

for model in get_models(get_app('schapen')):
    admin.site.register(model)
