# REDIRECCIONAR
from django.shortcuts import render
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
                    data.append(item)
                    
            
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

        return context
    success_url = reverse_lazy('index')
