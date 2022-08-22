# URL
from django.shortcuts import render

# Modelos
from apps.customers.models import Customer
from apps.products.models import Product, Category
from apps.users.models import User
from apps.invoices.models import Invoice, DetailInvoice


# CLASE
from apps.products.generador import ArchivoProducto as archvp
from apps.users.generador import ArchivoUsuario as archvu
from apps.customers.generador import ArchivoCliente as archvc
from apps.invoices.generador import ArchivoFacturas as archvf

# JSON
from django.http import JsonResponse


# DECORADORES
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# TEMPLATEVIEW
from django.views.generic import TemplateView

# FORMULAROP
from .forms import TestForm


###--MODULO DE INICIO--###
def index(request):

    archvp.subir(Product)
    archvu.subir(User)
    archvc.subir(Customer)
    archvf.subir(Invoice, DetailInvoice)
    

    template = 'index.html'
    context = {
        'title':'INICIO',
        'customer_count': Customer.objects.all().count(),
        'product_count': Product.objects.all().count(),
        'user_count': User.objects.all().count(),
        'invoice_count': Invoice.objects.all().count(),
        
        
    }
    return render(request,template,context)


###-- MODULO DE INFORMACION GENERAL--###
def about(request):
    template = 'about.html'
    context = {
        'title': 'Acerca de:'

    }
    return render(request, template, context)


###-- MODULO DE MANUAL DE USUARIO--###    
def help(request):
    template = 'help.html'
    context = {
        'title': 'Acerca de:'

    }
    return render(request, template, context)


class TestView(TemplateView):
    template_name = 'test.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_product_id':
                data = [{'id': '', 'text': '------------'}]
                for i in Product.objects.filter(cat_id=request.POST['id']):
                    data.append({'id': i.id, 'text': i.name, 'data': i.cat.toJSON()})
            elif action == 'autocomplete':
                data = []
                for i in Category.objects.filter(name__icontains=request.POST['term'])[0:10]:
                    item = i.toJSON()
                    item['text'] = i.name
                    data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Select Aninados | Django'
        context['form'] = TestForm()
        return context