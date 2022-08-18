from django import forms
from .models import Product

class productForm(forms.ModelForm):
    class Meta:
        model = Product

        fields = [
            'title',
            'description',
            'price',
            'image',
            'category',

        ]

        labels = {
            'title': 'Nombre',
            'description': 'Descripcion',
            'price': 'Precio',
            'image': 'Imagen',
            'category': 'Category',

        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'category': forms.CheckboxSelectMultiple(attrs={'type': 'checkbox'}),
            'image': forms.FileInput(attrs={'type':'checkbox', 'name':'image', 'type':'file', 'accept':'image',
            'class': 'form-control'}),
            'price': forms.TextInput(
                attrs={'class': 'form-control', 'type': 'number', 'step': '0.01', 'min': '1'}),

        }
