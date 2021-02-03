from django.contrib import admin
from django.urls import path, include
from tsv import views

urlpatterns = [
    path('', views.index)
]