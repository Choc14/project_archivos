#URL PARA ACCEDER AL ADMIN DE DJANGO
from django.contrib import admin

#CONFIGURANCION PARA MANEJAR LOS STATICS Y MEDIA
from django.conf.urls.static import static
from django.conf import settings

#VISTA
from . import views

#AGREGAR URLS
from django.urls import path, include



urlpatterns = [
    path('', views.index, name = 'index'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
