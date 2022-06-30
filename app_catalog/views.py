from django.views.generic import ListView, DetailView


class ItemList(ListView):
    pass


class ItemDetail(DetailView):

    def post(self, request):
        if 'commentary' in request.POST:
            pass

        elif 'add-to-cart' in request.POST:
            pass
