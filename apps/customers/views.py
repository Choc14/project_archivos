from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse_lazy

from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic.detail import DetailView

from .models import Customer
from .forms import customerForm

from .utils import breadcrumb

from .generador import ArchivoCliente as archivo

# Create your views here.
class customerList(ListView):
    template_name = 'customers/customer.html'
    queryset = Customer.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        archivo.subir(Customer)
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de Clientes'
        context['title'] = 'Cliente'
        context['breadcrumb'] = breadcrumb()


        return context

class customerCreate(CreateView):
    model = Customer
    form_class = customerForm
    template_name = 'customers/customerForm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar'
        context['message'] = 'Agregar'

        return context

    success_url = reverse_lazy('customers:Cliente')

class customerUpdate(UpdateView):
    model = Customer
    form_class = customerForm
    template_name = 'customers/customerForm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar'
        context['message'] = 'Editar'

        return context

    success_url = reverse_lazy('customers:Cliente')

class customerDelete(DeleteView):
    model = Customer
    template_name = 'customers/customerDelete.html'
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar'

        return context
    success_url = reverse_lazy('customers:Cliente')

class customerDetalle(DetailView):
    model = Customer
    template_name = 'customers/customerDetalle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle'
        context['message'] = 'Detalle'
        context['breadcrumb'] = breadcrumb()

        return context
