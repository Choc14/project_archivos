
# FORMULARIO DE DJANGO
from django import forms

# MODELOS
from .models import User

# LIBRERIA QUE SE ENCARGA DE CREAR USUARIOS
from django.contrib.auth.forms import UserCreationForm

###-- FORMULARIO PARA CAMBIAR ALGUNA INFORMACION DE UN USUARIO --#
class UpdateUserForm(forms.ModelForm):
    USER_TYPE = [
            ('USUARIO', 'USUARIO'),
            ('ADMINISTRADOR', 'ADMINISTRADOR')
    ]
    user_type = forms.ChoiceField(
        choices=USER_TYPE,
        required = False,
        label='Tipo de Usuario',
        widget=forms.Select(attrs={'class': 'form-control'}),
        )
    
    password1 = forms.CharField(
        label='CONTRASEÑA: ',        
        widget = forms.PasswordInput(attrs={'class': 'form-control'}),
        required = False,
        

    )
    password2 = forms.CharField(
        label='CONFIRMAR CONTRASEÑA: ',
        widget = forms.PasswordInput(attrs={'class': 'form-control'}),
        required = False,

    )

    class Meta:
        model = User

        fields = [
            'first_name',
            'last_name',
            'username',
            'email',            
            'user_type',
            'image',
            
        ]

        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'username': 'Usuario',
            'email': 'Correo',
            'image': 'Imagen de Usuario',
            
            
            
        }

        

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'type':'checkbox', 'name':'image', 'type':'file', 'accept':'image', 'class':'form-control'}),
               
            

        }

###-- FORMULARIO PARA CREAR Y REGISTRAR USUARIOS--#

class CreateUserForm(UserCreationForm):
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
    
    password1 = forms.CharField(
        label='CONTRASEÑA: ',
        widget = forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
        required = True,
       

    )
    password2 = forms.CharField(
        label='CONFIRMAR CONTRASEÑA: ',
        widget = forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
        required = True,       


    )

    class Meta:
        model = User

        fields = [
            'first_name',
            'last_name',
            'username',
            'email',            
            'user_type',
            'image',
            
        ]

        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'username': 'Usuario',
            'email': 'Correo',
            'image': 'Imagen de Usuario',
            
            
            
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'type':'checkbox', 'name':'image', 'type':'file', 'accept':'image', 'class':'form-control'}),
               
            

        }

###-- FORMULARIO PARA CREAR Y REGISTRAR USUARIOS--#
class RegistroForm(UserCreationForm):
    USER_TYPE = [
            ('USUARIO', 'USUARIO'),
            ('ADMINISTRADOR', 'ADMINISTRADOR')
    ]
    user_type = forms.ChoiceField(
        choices=USER_TYPE,
        required = False,
        label='Tipo de Usuario',
        widget=forms.Select(attrs={'class': 'form-control'}),
        )
    
    password1 = forms.CharField(
        label='CONTRASEÑA: ',
        widget = forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
        required = True,
       

    )
    password2 = forms.CharField(
        label='CONFIRMAR CONTRASEÑA: ',
        widget = forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
        required = True,       


    )

    class Meta:
        model = User

        fields = [
            'first_name',
            'last_name',
            'username',
            'email',            
            'user_type',
            'image',
            
        ]

        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'username': 'Usuario',
            'email': 'Correo',
            'image': 'Imagen de Usuario',
            
            
            
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'type':'checkbox', 'name':'image', 'type':'file', 'accept':'image', 'class':'form-control'}),
               
            

        }

###-- FORMULARIO PARA CAMBIAR LA CONTRASEÑA --###
class ChangePasswordForm(forms.Form):
    password1 = forms.CharField(
        label='NUEVA CONTRASEÑA: ',
        widget = forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
        required = True,
       

    )
    password2 = forms.CharField(
        label='CONFIRMAR CONTRASEÑA: ',
        widget = forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
        required = True,       


    )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('Contraseña no coinciden')
        return password2

###-- FORMULARIO PARA CAMBIAR EL USERNAME --###
class ChangeUserForm(forms.Form):
    username = forms.CharField(
        label='NUEVO USERNAME: ',
        widget = forms.TextInput(attrs={'class': 'form-control', }),
        required = True,
       

    )