# URL
from django.shortcuts import render

# Modelos
from apps.customers.models import Customer
from apps.products.models import Product
from apps.users.models import User

# CLASE
from apps.products.generador import ArchivoProducto as archvp
from apps.users.generador import ArchivoUsuario as archvu
from apps.customers.generador import ArchivoCliente as archvc


def index(request):

    archvp.subir()
    archvu.subir()
    archvc.subir()

    template = 'index.html'
    context = {
        'title':'INICIO',
        'customer_count': Customer.objects.all().count(),
        'product_count': Product.objects.all().count(),
        'user_count': User.objects.all().count,
        
    }
    return render(request,template,context)

def about(request):
    template = 'about.html'
    context = {
        'title': 'Acerca de:'

    }
    return render(request, template, context)
    
def help(request):
    template = 'help.html'
    context = {
        'title': 'Acerca de:'

    }
    return render(request, template, context)