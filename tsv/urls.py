from django.contrib import admin
from django.urls import path, include
from tsv import views

app_name = 'tsv'

urlpatterns = [
    path('', views.index, name='index'),
    path('answers/create/weather/', views.answers_weather, name='answers_weather'),
    path('answers/create/mood/', views.answers_mood, name='answers_mood'),
    path('answers/create/wake_up/', views.answers_wake_up, name='answers_wake_up'),
    path('answers/create/did_well/', views.answers_did_well, name='answers_did_well'),
    path('answers/create/happiness/', views.answers_happiness, name='answers_happiness'),
    path('answers/create/meal/', views.answers_meal, name='answers_meal'),
]