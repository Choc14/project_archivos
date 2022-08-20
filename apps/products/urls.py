from django.urls import path
from . import views

# DECORADOR
from django.contrib.auth.decorators import login_required
app_name = 'products'

urlpatterns = [

    path('', login_required(views.ProductoList.as_view()), name='Producto'),
    path('crear/', login_required(views.ProductoCreate.as_view()), name='Crear'),
    path('category/add/', login_required(views.CategoryCreate.as_view()), name='category_add'),
    path('actualizar/<int:pk>/', login_required(views.ProductoUpdate.as_view()), name='Actualizar'),
    path('eliminar/<int:pk>/', login_required(views.ProductoDelete.as_view()), name='Eliminar'),
    path('detalle/<int:pk>/', login_required(views.ProductoDetalle.as_view()), name='Detalle'),
    path('buscar/', login_required(views.ProductoSearch.as_view()), name = 'Buscar'),

]