from django.urls import path, re_path
from django.contrib import admin
from .views import index

urlpatterns = [
    re_path(r'^$', index, name='index'),
]