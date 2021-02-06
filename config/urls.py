from django.contrib import admin
from django.urls import path, include
from tsv import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('tsv/', include('tsv.urls')),
    path('common/', include('common.urls')),
]
