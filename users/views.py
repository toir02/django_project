from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import RegisterForm
from users.models import User
from users.sevices import send_verification_mail


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user_email = self.request.POST.get('email')
        send_verification_mail(user_email)
        return super().form_valid(form)
