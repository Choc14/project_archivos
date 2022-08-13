from django.urls import path
from . import views

# DECORADOR
from django.contrib.auth.decorators import login_required
app_name = 'customers'

urlpatterns = [

    path('', login_required(views.customerList.as_view()), name='Cliente'),
    path('crear/', views.customerCreate.as_view(), name='Crear'),
    path('actualizar/<int:pk>/', views.customerUpdate.as_view(), name='Actualizar'),
    path('eliminar/<int:pk>/', views.customerDelete.as_view(), name='Eliminar'),
    path('detalle/<int:pk>/', views.customerDetalle.as_view(), name='Detalle'),
]