
from django.urls import reverse

def breadcrumb(invoices = True):
    return [
        {'title': 'Facturas', 'active': invoices, 'url': reverse('invoices:list')}
    ]