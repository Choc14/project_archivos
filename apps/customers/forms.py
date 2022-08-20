###-- CREACION DE FORMULARIOS PARA EL RESPECTIVO MODELO --##

from cProfile import label
from django import forms
from .models import Customer, City

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
            'addres': 'Direccion',
            'phone_number': 'Telefono',
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
            'city': forms.Select(attrs={'class': 'form-control select2'}),
            'id_type': forms.Select(attrs={'class': 'form-control'}),


        }

class cityForm(forms.ModelForm):
    class Meta:
        model = City

        fields = [
            'name_city'
        ]

        labels = {
            'name_city': 'NOMBRE DE LA CIUDAD'
        }

        widgets = {
            'name_city': forms.TextInput(attrs={'class': 'form-control'}),
        }
