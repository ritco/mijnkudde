# hier definiëren we alle URLs die beginnen met schapen/


from django.conf.urls import url
from . import views

urlpatterns = [
    #voorbeeld: /
    url(r'^$', views.schapen_list, name = 'schapen_list'),
    #voorbeeld: /schaap/internnr123

    # MOET NOG VERDER UITGEWERKT WORDEN!!!!


]
