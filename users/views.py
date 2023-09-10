from django.shortcuts import render
from django.views.generic import CreateView

from users.forms import RegisterForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
