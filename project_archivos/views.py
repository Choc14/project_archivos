# URL
from django.shortcuts import render

def index(request):
    template = 'index.html'
    context = {
        'title':'INICIO',
        'message': 'HOLA MUNDO'
    }
    return render(request,template,context)