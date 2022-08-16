from django.urls import reverse

def breadcrumb(users = True):
    return [
        {'title': 'Usuarios', 'active': users, 'url': reverse('users:list')}
    ]