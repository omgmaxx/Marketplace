from django.views.generic import ListView, DetailView

from app_catalog.filters import ItemFilter
from app_catalog.models import Item


class ItemList(ListView):
    model = Item
    template_name = 'catalog/catalog.html'
    paginate_by = 8

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ItemFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs.select_related('cover_image', 'category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset

        # Limits for pagination list
        context['page_list_end'] = context['page_obj'].number + 5
        context['page_list_start'] = context['page_obj'].number - 5

        return context


class ItemDetail(DetailView):

    def post(self, request):
        if 'commentary' in request.POST:
            pass

        elif 'add-to-cart' in request.POST:
            pass
