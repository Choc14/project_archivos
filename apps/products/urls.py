from django.urls import path
from . import views

# DECORADOR
from django.contrib.auth.decorators import login_required
app_name = 'products'

urlpatterns = [

    path('', login_required(views.productoList.as_view()), name='Producto'),
    path('crear/', views.productoCreate.as_view(), name='Crear'),
    path('actualizar/<int:pk>/', views.productoUpdate.as_view(), name='Actualizar'),
    path('eliminar/<int:pk>/', views.productoDelete.as_view(), name='Eliminar'),
    path('detalle/<int:pk>/', views.productoDetalle.as_view(), name='Detalle'),

]