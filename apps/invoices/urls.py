# path de django
from django.urls import path

# VIEWS
from . import views

# DECORADOR
from django.contrib.auth.decorators import login_required
app_name = 'invoices'

urlpatterns = [
    path('add/', login_required(views.CreateInvoice.as_view()), name='add')
    
]