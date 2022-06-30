from django.views.generic import TemplateView, ListView, DetailView, UpdateView


class Cabinet(TemplateView):
    template_name = ''

    def form_valid(self, form):
        pass


class Profile(UpdateView):
    template_name = ''
    # model =
    # fields =

    def get_context_data(self, **kwargs):
        pass


class HistoryList(ListView):
    # model =
    pass


class HistoryDetail(DetailView):
    # model =
    pass

    def post(self, request):
        pass
