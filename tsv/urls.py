from django.contrib import admin
from django.urls import path, include
from .views import base_views, answers_views, my_page_views

app_name = 'tsv'

urlpatterns = [
    path('', base_views.index, name='index'),
    path('answers/detail/<int:answers_id>', base_views.detail, name='detail'),

    path('answers/create/weather/', answers_views.answers_weather, name='answers_weather'),
    path('answers/create/mood/', answers_views.answers_mood, name='answers_mood'),
    path('answers/create/wake_up/', answers_views.answers_wake_up, name='answers_wake_up'),
    path('answers/create/did_well/', answers_views.answers_did_well, name='answers_did_well'),
    path('answers/create/happiness/', answers_views.answers_happiness, name='answers_happiness'),
    path('answers/create/meal/', answers_views.answers_meal, name='answers_meal'),

    path('my_page/', my_page_views.my_page, name='my_page'),
    path('my_page/edit_profile/', my_page_views.edit_profile, name='edit_profile'),

]