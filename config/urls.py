from django.contrib import admin
from django.urls import path, include
from tsv import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tsv/', include('tsv.urls')),
]