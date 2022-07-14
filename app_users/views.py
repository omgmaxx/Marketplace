from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.db.transaction import atomic
from django.urls import reverse
from django.views.generic import CreateView

from app_users.forms import RegisterUserForm
from app_users.services.register import Register


class RegisterUser(CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = RegisterUserForm

    @atomic
    def form_valid(self, form):
        to_return = super().form_valid(form)
        register_call = Register()
        register_call.execute(form, self.request)
        return to_return

    def get_success_url(self):
        return reverse('main')


class LogIn(LoginView):
    redirect_authenticated_user = True
    template_name = 'users/login.html'


class LogOut(LoginRequiredMixin, LogoutView):
    template_name = 'users/logout.html'
