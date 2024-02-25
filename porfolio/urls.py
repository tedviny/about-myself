from django.conf.urls import include, url
from django.urls import path, re_path
from django.contrib import admin
from . import views

urlpatterns = [
    re_path(r'^$', home, name='index'),
]