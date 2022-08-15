
from django.urls import reverse

def breadcrumb(customers = True):
    return [
        {'title': 'Clientes', 'active': customers, 'url': reverse('customers:Cliente')}
    ]