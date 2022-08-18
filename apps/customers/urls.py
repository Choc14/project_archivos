from django.urls import path
from . import views

# DECORADOR
from django.contrib.auth.decorators import login_required
app_name = 'customers'

urlpatterns = [

    path('', login_required(views.CustomerList.as_view()), name='Cliente'),
    path('crear/', login_required(views.CustomerCreate.as_view()), name='Crear'),
    path('actualizar/<int:pk>/', login_required(views.CustomerUpdate.as_view()), name='Actualizar'),
    path('eliminar/<int:pk>/', login_required(views.CustomerDelete.as_view()), name='Eliminar'),
    path('detalle/<int:pk>/', login_required(views.CustomerDetalle.as_view()), name='Detalle'),
    path('buscar/', login_required(views.CustomerSearch.as_view()), name = 'Buscar'),
]