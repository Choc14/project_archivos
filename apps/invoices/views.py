# REDIRECCIONAR
from distutils.errors import PreprocessError
from math import factorial
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

# CRUD
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic.detail import DetailView
from django.db.models import Q
from django.db import transaction

# MODELOS
from .models import Invoice, DetailInvoice
from apps.products.models import Product
from apps.customers.models import Customer

# FORMULARIOS
from .forms import InvoiceForm

# JSON
import json
from django.http import JsonResponse

# Decorador
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


class CreateInvoice(CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoices/create.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_products':
                data = []
                prods = Product.objects.filter(title__icontains=request.POST['term'])[0:10]
                for i in prods:
                    item = i.toJSON()
                    item['value'] = i.title
                    item['text'] = i.title
                    data.append(item)
            elif action == 'add':
                with transaction.atomic():
                    vents = json.loads(request.POST['vents'])
                    print(vents)

                    cliente = vents['customer']
                    fecha = vents['created_at']
                    subtotal = float(vents['subtotal'])
                    iva = float(vents['iva'])
                    total = float(vents['total'])
                    cl = get_object_or_404(Customer,id = cliente)
                    

                    invoice = Invoice(customer=cl,created_at=fecha, subtotal=subtotal, iva = iva, total=total )                   
                    
                    invoice.save()

                    for i in vents['products']:
                        fact = invoice.id
                        fact_id = get_object_or_404(Invoice,id = fact)

                        prodcuto = i['id']
                        prod_id = get_object_or_404(Product,id = prodcuto)

                        cantidad = int(i['quantity'])
                        precio = float(i['price'])
                        d_subtotal = float(i['subtotal'])

                        detail = DetailInvoice(invoice=fact_id, product=prod_id,quantity=cantidad,price=precio,subtotal=d_subtotal)
                        detail.save()

            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nueva Factura'
        context['action'] = 'add'
        context['message'] = 'Nueva Factura'
        context['det'] = []
        context['factura'] = True

        return context
    success_url = reverse_lazy('invoices:list')

class ListInvoice(ListView):

    template_name = 'invoices/list.html'
    queryset = Invoice.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['title'] = 'FACTURAS'
        context['message'] = 'Listado de facturas'
        return context
