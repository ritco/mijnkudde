# coding=utf-8

"""mijnkuddeproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin
from schapen import views as schapen_views
from django.contrib.auth import views as auth_views

urlpatterns = [

    url(r'^bedrijf/', include('schapen.urls', namespace='schapen')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, name = 'login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'bedrijf/logged_out.html'}, name = 'logout'),
    url(r'^$', include('cms.urls', namespace='cms')),

]
