"""bison_accelerate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	url(r'^$', views.index_view, name="index"),
	url(r'^transfer$', views.transfer_view, name="transfer"),
	url(r'^all-clients$', views.all_clients_view, name="all_clients"),
    url(r'^transfer_detailed$', views.detailed_transfer_view, name="detailed-transfer"),
    url(r'^transfer_amount$', views.mid_transfer_view, name="mid-transfer")
]
