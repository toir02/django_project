from django.contrib.auth.views import LoginView
from django.urls import path

from users.apps import UsersConfig
from users.views import *

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('register/', RegisterView.as_view(template_name='users/register.html'), name='register'),
    path('verification/', verification_user, name='verification'),
]
