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

# MODELOS
from .models import Customer
from .forms import customerForm

# BREADCRUMB
from .utils import breadcrumb

# GENERADOR DE TXT
from .generador import ArchivoCliente as archivo

# Create your views here.
class CustomerList(ListView):
    template_name = 'customers/customer.html'
    queryset = Customer.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        archivo.subir(Customer)
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de Clientes'
        context['title'] = 'Cliente'
        context['breadcrumb'] = breadcrumb()


        return context

class CustomerCreate(CreateView):
    model = Customer
    form_class = customerForm
    template_name = 'customers/customerForm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar'
        context['message'] = 'Agregar'

        return context

    success_url = reverse_lazy('customers:Cliente')

class CustomerUpdate(UpdateView):
    model = Customer
    form_class = customerForm
    template_name = 'customers/customerForm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar'
        context['message'] = 'Editar'

        return context

    success_url = reverse_lazy('customers:Cliente')

class CustomerDelete(DeleteView):
    model = Customer
    template_name = 'customers/customerDelete.html'
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar'

        return context
    success_url = reverse_lazy('customers:Cliente')

class CustomerDetalle(DetailView):
    model = Customer
    template_name = 'customers/customerDetalle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle'
        context['message'] = 'Detalle'
        context['breadcrumb'] = breadcrumb()

        return context

class CustomerSearch(ListView):
    template_name = 'customers/customerBuscar.html'

    def get_queryset(self):
        filters = Q(first_name__icontains=self.query()) | Q(city__icontains=self.query()) | Q(id_type__icontains=self.query())
        return Customer.objects.filter(filters)

    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['title'] = 'Buscar'
        context['count'] = context['customer_list'].count()
        context['breadcrumb'] = breadcrumb()

        return context
