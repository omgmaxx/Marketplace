from django.views.generic import ListView, DetailView

from app_cart.services.adding_item_to_cart import AddingItemToCart
from app_catalog.filters import ItemFilter
from app_catalog.models import Item


class ItemList(ListView):
    model = Item
    template_name = 'catalog/catalog.html'
    paginate_by = 8
    paginate_list_range = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ItemFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs.select_related('cover_image', 'category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        # Filter context
        context['filter'] = self.filterset

        # Pagination context
        context['page_list_end'] = context['page_obj'].number + self.paginate_list_range + 1
        context['page_list_start'] = context['page_obj'].number - self.paginate_list_range - 1

        # Ordering context
        context['ordering'] = self.request.GET.get('ordering')
        context['order_variants'] = {
            'popularity': 'Popularity',
            'price': 'Price',
            'commentaries': 'Commentaries',
            'novelty': 'Novelty'
        }
        context['asc'] = self.request.GET.get('asc')

        return context

    def get_ordering(self):
        ordering = self.request.GET.get('ordering')
        asc = self.request.GET.get('asc')
        if asc == 'false':
            ordering = ''.join(('-', ordering))
        return ordering

    def post(self, request, *args, **kwargs):
        added_item_id = request.POST['add-to-cart']
        if added_item_id:
            adding = AddingItemToCart()
            adding.execute(added_item_id, request.user.id)
        return self.get(request)



class ItemDetail(DetailView):

    def post(self, request):
        if 'commentary' in request.POST:
            pass

        elif 'add-to-cart' in request.POST:
            pass
