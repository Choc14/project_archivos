# URL
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse


# LIBRERIAS PARA EL CRUD
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# FORMS
from .forms import RegistroForm

# Login
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

# Decoradores
from .decoradores import *

# Modulos
from django.contrib.auth.models import User

# Create your views here.

class SignUp(user_authenticate,CreateView):
    '''
    MODULO PARA REGISTRO DE USUARIOS
    '''
    model = User
    form_class = RegistroForm    
    template_name = 'users/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Register'
        context['messages.success'] = 'BIENVENIDO'
       

        return context

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        messages.success(self.request, 'USUARIO CREADO EXITOSAMENTE')
        return redirect('index')
        #return redirect('perfilUsuario')

    def handle_no_permission(self):
        '''
        Si el usuario esta registrado lo regresa al inicio
        :return:
        '''
        return HttpResponseRedirect(reverse('index'))

# login
def login_view(request):
    
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username') #diccionario
        password = request.POST.get('password') #None

        user = authenticate(username=username, password=password)#None
        if user:
            login(request, user)
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET['next'])
            
            '''
            if user.is_superuser:
                messages.success(request, 'Bienvenido ADMINISTRADOR: {}'.format(user.username))
                return redirect('perfilAdmin')
            else:
                messages.success(request, 'Bienvenido USUARIO: {}'.format(user.username))
                return redirect('perfilUsuario')
            '''
            
            return redirect('index')

        else:
            messages.error(request, 'Usuario o contraseña no validos')

    return render(request, "users/login.html", {
        'title':'LOGIN',
       
    })

# logout
def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente')
    return redirect('login')    