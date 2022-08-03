# URL
from django.shortcuts import render

def index(request):    
    template = 'index.html'
    context = {
        'title':'INICIO',
        
    }
    return render(request,template,context)