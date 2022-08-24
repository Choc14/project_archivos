# REDIRECCIONAR
from django.shortcuts import render,redirect
from django.urls import reverse_lazy

# CRUD
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic.detail import DetailView
from django.db.models import Q

# MODELOS
from .models import Customer, City, Id

# FORMULARIOS
from .forms import customerForm, cityForm, IdForm

# BREADCRUMB
from .utils import breadcrumb

# GENERADOR DE TXT
from .generador import ArchivoCliente as archivo

# JSON
import json
from django.http import JsonResponse

# Decorador
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


###-- MODULO QUE ENLISTA A LOS CLIENTES--###
class CustomerList(ListView):
    template_name = 'customers/customer.html'
    queryset = Customer.objects.all().order_by('-id')
    paginate_by = 5

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {'vaya':'as'}
        return JsonResponse(data, safe= False)

    def get_context_data(self, **kwargs):
        archivo.subir(Customer)
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de Clientes'
        context['title'] = 'Cliente'
        context['breadcrumb'] = breadcrumb()
        


        return context


###-- MODULO QUE CREA A LOS CLIENTES--###
class CustomerCreate(CreateView):
    model = Customer
    form_class = customerForm
    template_name = 'customers/customerForm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar'
        context['message'] = 'Agregar'        
        context['count'] = Id.objects.all().count()        

        return context

    success_url = reverse_lazy('customers:Cliente')


###-- MODULO QUE CREA A CIUDADES--###
class CityCreate(CreateView):
    model = City
    form_class = cityForm
    template_name = 'city/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar'
        context['message'] = 'Agregar'
        

        return context

    success_url = reverse_lazy('customers:Crear')

###-- MODULO QUE CERA A CIUDADES--###
class IdCreate(CreateView):
    model = Id
    form_class = IdForm
    template_name = 'Id/create.html'

    def get(self, request, *args, **kwargs):
        count = Id.objects.all().count()
        if count < 2:
            context = {
                'form':self.form_class,
                'title':'Agregar',
                'message':'Agregar'
            }
            return render(request, self.template_name, context)
        else:
            return redirect('index')
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar'
        context['message'] = 'Agregar'

        return context

    success_url = reverse_lazy('customers:Crear')


###-- MODULO QUE MODIFICA ALGUN CLIENTE--###
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


###-- MODULO QUE ELIMINA ALGUN CLIENTE--###
class CustomerDelete(DeleteView):
    model = Customer
    template_name = 'customers/customerDelete.html'
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar'

        return context
    success_url = reverse_lazy('customers:Cliente')


###-- MODULO QUE DETALLA ALGUN CLIENTE--###
class CustomerDetalle(DetailView):
    model = Customer
    template_name = 'customers/customerDetalle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle'
        context['message'] = 'Detalle'
        context['breadcrumb'] = breadcrumb()

        return context


###-- MODULO QUE BUSCA A LOS CLIENTES--###
class CustomerSearch(ListView):
    template_name = 'customers/customerBuscar.html'

    def get_queryset(self):
        filters = Q(first_name__icontains=self.query()) | Q(last_name__icontains=self.query())
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
