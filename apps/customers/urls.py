from django.urls import path
from . import views

# DECORADOR
from django.contrib.auth.decorators import login_required
app_name = 'customers'

urlpatterns = [

    path('', login_required(views.customerList.as_view()), name='Cliente'),
    path('crear/', login_required(views.customerCreate.as_view()), name='Crear'),
    path('actualizar/<int:pk>/', login_required(views.customerUpdate.as_view()), name='Actualizar'),
    path('eliminar/<int:pk>/', login_required(views.customerDelete.as_view()), name='Eliminar'),
    path('detalle/<int:pk>/', login_required(views.customerDetalle.as_view()), name='Detalle'),
]