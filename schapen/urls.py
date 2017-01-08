# coding=utf-8

# hier definiëren we alle URLs die beginnen met bedrijf (dit komt na login later)

from django.conf.urls import url
from . import views
from schapen import views as schapen_views

urlpatterns = [
    #voorbeeld: /
    url(r'^$', schapen_views.bedrijf_index, name='schapen'),
    # voorbeeld: /schaap/internnr123
    url(r'/aanwezige_schapen^$', schapen_views.bedrijf_aanwezige_schapen, name='schapen'),
    # MOET NOG VERDER UITGEWERKT WORDEN!!!!


]
