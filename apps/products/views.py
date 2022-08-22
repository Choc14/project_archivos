
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
from .models import Product, Category

# FORMULARIOS
from .forms import productForm, categoryForm

# CLASES
from .generador import ArchivoProducto as archivo

# EXTRAS
from .utils import breadcrumb

# Create your views here.
class ProductoList(ListView):
    template_name = 'products/product.html'
    queryset = Product.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):   
        archivo.subir(Product)   
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de Productos'
        context['title'] = 'Producto'
        context['breadcrumb'] = breadcrumb()


        return context

class ProductoCreate(CreateView):
    model = Product
    form_class = productForm
    template_name = 'products/productForm.html'

    

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar'
        context['message'] = 'Agregar'

        return context

    success_url = reverse_lazy('products:Producto')


class CategoryCreate(CreateView):
    model = Category
    form_class = categoryForm
    template_name = 'category/create.html'

    

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar'
        context['message'] = 'Agregar'

        return context

    success_url = reverse_lazy('products:Producto')

class ProductoUpdate(UpdateView):
    model = Product
    form_class = productForm
    template_name = 'products/productForm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar'
        context['message'] = 'Editar'

        return context

    success_url = reverse_lazy('products:Producto')

class ProductoDelete(DeleteView):
    model = Product
    template_name = 'products/productDelete.html'
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar'
        

        return context
    success_url = reverse_lazy('products:Producto')

class ProductoDetalle(DetailView):
    model = Product
    template_name = 'products/productDetalle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle'
        context['message'] = 'Detalle'
        context['breadcrumb'] = breadcrumb()

        return context

class ProductoSearch(ListView):
    template_name = 'products/productBuscar.html'

    def get_queryset(self):
        filters = Q(title__icontains=self.query())
        return Product.objects.filter(filters)

    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['title'] = 'Buscar'
        context['count'] = context['product_list'].count()
        context['breadcrumb'] = breadcrumb()

        return context
