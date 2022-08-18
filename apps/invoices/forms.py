# GENERADOR DE FORMULARIOS
from django import forms

# MODELOS
from .models import Invoice

# Tiempo
from datetime import datetime

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice

        fields = [
            'customer',            
            'iva',
            'subtotal',
            'total',
            'created_at'
        ]

        labels = {
            'customer': 'CLIENTE',            
            'iva': 'IVA',
            'subtotal': 'SUBTOTAL',
            'total': 'TOTAL',
            'created_at': 'FECHA DE VENTA'
        }
        
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control select2'}),            
            'iva': forms.TextInput(attrs={'class': 'form-control'}),
            'subtotal': forms.TextInput(attrs={'readonly': True,'class': 'form-control'}),
            'total': forms.TextInput(attrs={'readonly': True,'class': 'form-control'}),
            'created_at': forms.DateInput(format='%Y-%m-%d', attrs={'value': datetime.now().strftime('%Y-%m-%d'), 'autocomplete': 'off',
            'class': 'form-control datetimepicker-input','id': 'created_at','data-target': '#created_at','data-toggle': 'datetimepicker',
            
            'disabled':'disabled'}),

        }
       