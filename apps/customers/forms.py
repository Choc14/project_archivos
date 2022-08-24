###-- CREACION DE FORMULARIOS PARA EL RESPECTIVO MODELO --##
from django import forms



from .models import Customer, City, Id


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
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'type':'number'}),
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


class IdForm(forms.ModelForm):
    class Meta:
        model = Id

        fields = [
            'id_type'
        ]

        labels = {
            'id_type': 'Tipo de identificacion'
        }

        widgets = {
            'id_type': forms.TextInput(attrs={'class': 'form-control'}),
        }