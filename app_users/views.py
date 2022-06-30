from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView


class RegisterUser(CreateView):
    # model = User
    template_name = ''

    def form_valid(self, form):
        # +profile logic
        pass


class LogIn(LoginView):
    redirect_authenticated_user = True
    template_name = ''


class LogOut(LogoutView):
    template_name = ''


class EditUser(UpdateView):
    template_name = ''

    def get_context_data(self, **kwargs):
        pass

    def form_valid(self, form):
        pass
