# path de django
from django.urls import path

# VIEWS
from . import views

# DECORADOR
from django.contrib.auth.decorators import login_required

app_name = 'invoices'

urlpatterns = [
    path('', login_required(views.ListInvoice.as_view()), name='list'),
    path('add/', login_required(views.CreateInvoice.as_view()), name='add'),
    path('detail/<int:pk>', login_required(views.detailInvoice), name='detail'),
    path('delete/<int:pk>', login_required(views.deleteInvoice), name='delete'),
    path('pdf/<int:pk>',login_required(views.InvoicePDF.as_view()), name='pdf'),
 
]