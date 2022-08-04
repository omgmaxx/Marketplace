from distutils.util import strtobool

from django.db.models import Max
from django.views.generic import ListView, DetailView

from app_catalog.filters import ItemFilter
from app_catalog.models import Item, Tag, Manufacturer, Category


class ItemList(ListView):
    model = Item
    template_name = 'catalog/catalog.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ItemFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context


class ItemDetail(DetailView):

    def post(self, request):
        if 'commentary' in request.POST:
            pass

        elif 'add-to-cart' in request.POST:
            pass
