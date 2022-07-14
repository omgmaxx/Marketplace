from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group

from app_users.models import Profile


class Register:

    def _create_user(self, form):
        user = form.save()
        user.groups.add(Group.objects.get(name='Customer'))
        return user

    def _create_profile(self, user):
        Profile.objects.create(user=user)

    def _login_user(self, form, request):
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request, user)

    def execute(self, form, request):
        user = self._create_user(form)
        self._create_profile(user)
        self._login_user(form, request)
