from django.contrib import admin
from django.urls import path, include
from tsv import views

app_name = 'tsv'

urlpatterns = [
    path('', views.index),
    path('answers/create/', views.answers_create, name='answers_create')
]