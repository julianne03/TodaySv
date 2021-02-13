from django.contrib import admin
from django.urls import path, include
from tsv.views import base_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', base_views.index, name='index'),
    path('admin/', admin.site.urls),
    path('tsv/', include('tsv.urls')),
    path('common/', include('common.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)