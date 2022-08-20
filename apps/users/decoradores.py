# Decoradores
from django.contrib.auth.mixins import UserPassesTestMixin

class user_authenticate(UserPassesTestMixin):
    '''
    Evalua si el usuario esta identificado
    '''
    def test_func(self):
        if not self.request.user.is_authenticated:
            return True
        else:
            return False

class user_admin(UserPassesTestMixin):
    '''
    Evalua si el usuario es un administrador
    '''
    def test_func(self):
        if self.request.user.is_superuser:
            
            return True
        else:
            return False

