from django.db import models
from django.contrib.auth.models import AbstractUser

from project_archivos.settings import MEDIA_URL, STATIC_URL

# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to='users/', null=True, blank=True)

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/usuario.png')
    
    def get_type_user(self):
        if self.is_superuser:
            return f'ADMINISTRADOR'
        return f'USUARIO'
    
    def get_full_name(self):
        if self.first_name == '' and self.last_name == '':
            return f'----'
        return '{} {}'.format(self.first_name, self.last_name)
        

    
