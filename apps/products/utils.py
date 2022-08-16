
from django.urls import reverse

def breadcrumb(products = True):
    return [
        {'title': 'Productos', 'active': products, 'url': reverse('products:Producto')}
    ]