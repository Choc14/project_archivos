# GENERADOR DE FORMULARIOS
from django import forms

# MODELOS
from .models import Invoice


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice

        fields = [
            'customer',            
            'iva',
            'subtotal',
            'total'
        ]

        labels = {
            'customer': 'Cliente',            
            'iva': 'IVA',
            'subtotal': 'SubTotal',
            'total': 'TOTAL'
        }
        
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),            
            'iva': forms.TextInput(attrs={'class': 'form-control'}),
            'subtotal': forms.TextInput(attrs={'readonly': True,'class': 'form-control'}),
            'total': forms.TextInput(attrs={'readonly': True,'class': 'form-control'})

        }
       