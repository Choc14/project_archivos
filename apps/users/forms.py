from .models import User
from django.contrib.auth.forms import UserCreationForm

from django import forms


class RegistroForm(UserCreationForm):
    USER_TYPE = [
            ('USUARIO', 'USUARIO'),
            ('ADMINISTRADOR', 'ADMINISTRADOR')
    ]
    user_type = forms.ChoiceField(
        choices=USER_TYPE,
        required = True,
        label='Tipo de Usuario',
        widget=forms.Select(attrs={'class': 'form-control'}),
        )

    class Meta:
        model = User

        fields = [
            'first_name',
            'last_name',
            'username',
            'email',            
            'user_type',
            'image'
        ]

        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'username': 'Usuario',
            'email': 'Correo',
            'image': 'Imagen de Usuario'
            
            
        }

        

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'type':'checkbox', 'name':'image', 'type':'file', 'accept':'image'}),
                 
            

        }


