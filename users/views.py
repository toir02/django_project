import random

from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import RegisterForm
from users.models import User
from users.services import send_verification_mail


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'users/register.html'

    def form_valid(self, form):
        key = random.randint(1000, 9999)
        self.request.session['key'] = key
        user_email = self.request.POST.get('email')
        send_verification_mail(user_email, key)
        return super().form_valid(form)
