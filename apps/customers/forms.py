from django import forms
from .models import Customer
from .models import City
from .models import Id

class customerForm(forms.ModelForm):
    class Meta:
        model = Customer

        fields = [
            'first_name',
            'last_name',
            'addres',
            'phone_number',
            'date_birth',
            'city',
            'id_type',



        ]

        labels = {
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'addres': 'Dirección',
            'phone_number': 'Teléfono',
            'date_birth': 'Fecha de nacimiento',
            'city': 'Ciudad',
            'id_type': 'Id',


        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'addres': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'date_birth': forms.TextInput(attrs = {'class': 'form-control', 'type': 'date'}),
            'city': forms.Select(attrs={'class': 'form-control'}),
            'id_type': forms.Select(attrs={'class': 'form-control'}),


        }




