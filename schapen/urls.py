# coding=utf-8

# hier definiëren we alle URLs die beginnen met bedrijf (dit komt na login later)

from django.conf.urls import url
from . import views
from schapen import views as schapen_views

app_name = 'schapen'

urlpatterns = [
    #voorbeeld: /

    # voorbeeld: /schaap/internnr123
    url(r'^aanwezige_schapen', schapen_views.bedrijf_aanwezige_schapen, name = 'bedrijf_aanwezige_schapen'),
    url(r'^alle_schapen', schapen_views.bedrijf_alle_schapen, name = 'bedrijf_alle_schapen'),
    url(r'^schaap_toevoegen', schapen_views.bedrijf_schaap_toevoegen, name = 'bedrijf_schaap_toevoegen'),
    url(r'^$', schapen_views.bedrijf_index, name='bedrijf_index'),


]
