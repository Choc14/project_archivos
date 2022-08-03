from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [

    path('signUp/', views.SignUp.as_view(), name = 'signUp'),
    path('accounts/login/',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'), 
    

]