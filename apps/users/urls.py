from django.urls import path
from . import views

# DECORADOR
from django.contrib.auth.decorators import login_required

app_name = 'users'

urlpatterns = [

    path('signUp/', views.SignUp.as_view(), name = 'signUp'),
    path('accounts/login/',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('users/create/', login_required(views.CreateUser.as_view()), name='create'),
    path('users/list/', login_required(views.ListUser.as_view()), name='list'), 
    path('users/delete/<int:pk>/', login_required(views.DeleteUser.as_view()), name='delete'),
    path('users/update/<int:pk>/', login_required(views.UpdateUser.as_view()), name='update'),
    path('users/change_username/<int:pk>/', login_required(views.ChangeUsername.as_view()), name='update_p'),
    path('users/detail/<int:pk>/', login_required(views.DetailUser.as_view()), name='detail' ),
    path('users/search/', login_required(views.UserSearch.as_view()), name = 'search'),

]