# coding=utf-8

# hier definiëren we alle URLs die beginnen met schapen

from django.conf.urls import url
from . import views

urlpatterns = [
    #voorbeeld: /
    url(r'^$', schapen_views.bedrijf_index, name='index'),
    # voorbeeld: /schaap/internnr123

    # MOET NOG VERDER UITGEWERKT WORDEN!!!!


]
