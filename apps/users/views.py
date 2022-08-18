# URL
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.db.models import Q

# LIBRERIAS PARA EL CRUD
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# FORMS
from .forms import RegistroForm, UpdateUserForm

# Login
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

# Decoradores
from .decoradores import *
from .bread import breadcrumb

# Modulos
from .models import User

# Clases
from .generador import ArchivoUsuario as archivo

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
        context['info'] = 'Registrar' 
       

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
            
            
            if user.is_superuser:
                messages.success(request, 'Bienvenido ADMINISTRADOR: {}'.format(user.username))
               
            else:
                messages.success(request, 'Bienvenido USUARIO: {}'.format(user.username))
               
           
            
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
    return redirect('users:login')

class CreateUser(user_admin, CreateView):
    
    model = User
    form_class = RegistroForm    
    template_name = 'users/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Crear Usuario'
        context['info'] = 'Crear Usuario' 
        
        return context
    
    def form_valid(self, form):
        form.save()


        return redirect('users:list')

  

    def handle_no_permission(self):
        '''
        Si el usuario esta registrado lo regresa al inicio
        :return:
        '''
        return HttpResponseRedirect(reverse('index'))

class ListUser(ListView):
    queryset = User.objects.all().order_by('-id')
    template_name = 'users/list.html'
    def get_context_data(self, **kwargs):
        archivo.subir(User)
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de Usuarios'
        context['title'] = 'Usuarios'
        context['breadcrumb'] = breadcrumb()
        return context

class DeleteUser(user_admin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar'
        context['update'] = True
        

        return context

    def handle_no_permission(self):
        '''
        Si el usuario esta registrado lo regresa al inicio
        :return:
        '''
        return HttpResponseRedirect(reverse('index'))

    success_url = reverse_lazy('users:list')



        

class UpdateUser(user_admin, UpdateView):
    model = User
    form_class = UpdateUserForm
    template_name = 'users/update.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar'
        context['update'] = True
        context['info'] = 'Actualizar'
                

        return context

    def handle_no_permission(self):
        '''
        Si el usuario esta registrado lo regresa al inicio
        :return:
        '''
        return HttpResponseRedirect(reverse('index'))
    success_url = reverse_lazy('users:list')

class ChangeUsername(UpdateView):
    model = User
    form_class = UpdateUserForm
    template_name = 'users/change_username.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Cambiar Usuario'
        context['update'] = True
        context['info'] = 'Actualizar'
                

        return context

  
    success_url = reverse_lazy('users:list')

class DetailUser(DetailView):
    model = User
    template_name = 'users/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalle'
        context['message'] = 'Detalle'
        context['update'] = True
        context['breadcrumb'] = breadcrumb()

        return context

class UserSearch(ListView):
    template_name = 'users/search.html'

    def get_queryset(self):
        filters = Q(username__icontains=self.query()) | Q(email__icontains=self.query()) | Q(user_type__icontains=self.query())
        return User.objects.filter(filters)

    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['title'] = 'Buscar'
        context['count'] = context['user_list'].count()
        context['breadcrumb'] = breadcrumb()

        return context