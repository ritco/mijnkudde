from django.contrib import admin

# Register your models here.

# aanpassing is nodig om de schapen gegevens in de admin backend te zien

from .models import schapen

class reviewSchapen(admin.ModelAdmin):
        model = Review
        list_display = ('schapen', 'usern_name', 'pub_date')
        list_filter = ['pub_date', 'usern_name']

admin.site.register(reviewSchapen)
