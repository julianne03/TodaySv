from django.contrib import admin
from django.urls import path, include
from tsv import views

app_name = 'tsv'

urlpatterns = [
    path('', views.index, name='index'),
    path('answers/create/weather/', views.answers_weather, name='answers_weather'),
    path('answers/create/mood/', views.answers_mood, name='answers_mood'),
]