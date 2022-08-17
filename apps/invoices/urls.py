from django.urls import path
from . import views
app_name = 'invoices'

urlpatterns = [
    path('add/', views.CreateInvoice.as_view(), name='add')
    
]