from django.views.generic import TemplateView


class Cart(TemplateView):

    def get_context_data(self, **kwargs):
        pass

    def post(self, request):
        if 'add' in request.POST:
            pass

        elif 'sub' in request.POST:
            pass

        elif 'delete' in request.POST:
            pass
