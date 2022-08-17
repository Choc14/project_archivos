
# LIBRERIAS PARA REDERICCIONAR
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

# LIBRERIAS PARA CRUD
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic.detail import DetailView
from django.db.models import Q

# MODELOS
from .models import Product

# FORMULARIOS
from .forms import productForm

# CLASES
from .generador import ArchivoProducto as archivo

# EXTRAS
from .utils import breadcrumb

# Create your views here.
class productoList(ListView):
    template_name = 'products/product.html'
    queryset = Product.objects.all().order_by('-id')

 
        

    def get_context_data(self, **kwargs):   
        archivo.subir()   
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de Productos'
        context['title'] = 'Producto'
        context['breadcrumb'] = breadcrumb()


        return context

class productoCreate(CreateView):
    model = Product
    form_class = productForm
    template_name = 'products/productForm.html'

    

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar'
        context['message'] = 'Agregar'

        return context

    success_url = reverse_lazy('products:Producto')

class productoUpdate(UpdateView):
    model = Product
    form_class = productForm
    template_name = 'products/productForm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar'
        context['message'] = 'Editar'

        return context

    success_url = reverse_lazy('products:Producto')

class productoDelete(DeleteView):
    model = Product
    template_name = 'products/productDelete.html'
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar'
        

        return context
    success_url = reverse_lazy('products:Producto')

class productoDetalle(DetailView):
    model = Product
    template_name = 'products/productDetalle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle'
        context['message'] = 'Detalle'
        context['breadcrumb'] = breadcrumb()

        return context
