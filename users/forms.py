from django.contrib.auth.forms import UserCreationForm
from django import forms

from users.models import User


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)


class VerificationForm(forms.Form):
    key = forms.IntegerField(label='Введите ключ для верификации')


class ResetPasswordForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email',)
