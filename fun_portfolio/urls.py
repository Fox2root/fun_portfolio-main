"""fun_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from basic_app import views
from contact import views as contact_views
from django.urls import path


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name ='index'),   
    url(r'^basic_app/', include('basic_app.urls')), 
    url(r'^experience_app/', include('experience_app.urls')),       
    url(r'^subscribe/$', views.subscribe, name='subscribe'),
    path('contact/', contact_views.contact_view, name='contact'),
]

