import random

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView as BaseLoginView

from users.forms import *
from users.models import User
from users.services import *


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'users/register.html'

    def form_valid(self, form):
        user = form.save()
        user.save()

        key = random.randint(1000, 9999)
        self.request.session['key'] = key
        user_email = self.request.POST.get('email')
        send_verification_mail(user_email, key)

        form.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('users:verification')


def verification_user(request):
    key = request.session.get('key')
    user = request.user
    if request.method == 'POST':
        form = VerificationForm(request.POST)
        if form.is_valid():
            entered_key = form.cleaned_data['key']
            if entered_key == key:
                user.is_active = True
                return redirect('users:success_verification')
    else:
        form = VerificationForm()
    return render(request, 'users/verification.html', {'form': form})


def success_verification(request):
    return render(request, 'users/verification_success.html')


class LoginView(BaseLoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('catalog:product')


@login_required
def set_new_password(request):
    form = ResetPasswordForm()
    if request.method == 'POST':
        new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
        user_email = request.user.email
        send_new_password(user_email, new_password)
        request.user.set_password(new_password)
        request.user.save()
    return render(request, 'users/password_reset.html', {'form': form})

