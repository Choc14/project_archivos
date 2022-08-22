#URL PARA ACCEDER AL ADMIN DE DJANGO
from django.contrib import admin

#CONFIGURANCION PARA MANEJAR LOS STATICS Y MEDIA
from django.conf.urls.static import static
from django.conf import settings

#VISTA
from . import views

#AGREGAR URLS
from django.urls import path, include

# DECORADOR
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('', login_required(views.index), name = 'index'),
    path('about/', views.about, name='about'),
    path('help/', views.help, name='help'),
    path('',include('apps.users.urls')),
    path('products/',include('apps.products.urls')),
    path('customers/',include('apps.customers.urls')),
    path('invoices/',include('apps.invoices.urls')),
    path('test/', views.TestView.as_view(), name='test'),
    path('admin/', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
