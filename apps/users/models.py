###---APARTADO DEL MODELO DE LA TABLA PARA DICHO MODELO--###

# ORM DE DJANGO
from django.db import models
from django.db.models.signals import pre_save

# MODELO
from django.contrib.auth.models import AbstractUser


# SETTINGS OF PROJECT
from project_archivos.settings import MEDIA_URL, STATIC_URL

# TIEMPO
from datetime import datetime

# Create your models here.
class User(AbstractUser):
    USER_TYPE = [
        ('USUARIO', 'USUARIO'),
        ('ADMINISTRADOR', 'ADMINISTRADOR')
    ]

    image = models.ImageField(upload_to='users/', null=True, blank=True)
    user_type = models.CharField(choices=USER_TYPE, default='USUARIO', null=True, blank=True, max_length=100)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/usuario.png')
    
    def get_type_user(self):
        if self.is_superuser:
            return f'ADMINISTRADOR'
        return f'USUARIO'
    
   
    
    def get_full_name(self):
        if self.first_name == '' or self.last_name == '':
            return f'----'
        return '{} {}'.format(self.first_name, self.last_name)


def set_user_type(sender, instance, *args, **kwargs):
    if instance.user_type == 'ADMINISTRADOR':
        instance.is_superuser = True
        instance.is_staff = True
        instance.is_active = True
    else:
        instance.is_superuser = False
        instance.is_staff = False
        instance.is_active = True


    
pre_save.connect(set_user_type, sender=User)