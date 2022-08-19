from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView, UpdateView

from app_catalog.models import Item


class Cabinet(TemplateView):
    template_name = 'cabinet/cabinet.html'

    def form_valid(self, form):
        pass


class Profile(UpdateView):
    template_name = 'cabinet/profile.html'
    model = User
    context_object_name = 'current_user'
    fields = '__all__'

    def get(self, request, **kwargs):
        self.object = User.objects.get(username=self.request.user)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        pass


class HistoryList(ListView):
    model = Item #placeholder
    template_name = 'cabinet/historyorder.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['range'] = range(3)
        return context


class HistoryDetail(DetailView):
    # model =
    pass

    def post(self, request):
        pass
