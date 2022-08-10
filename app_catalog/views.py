from django.db.models import Count
from django.views.generic import ListView, DetailView

from app_cart.services.adding_item_to_cart import AddingItemToCart
from app_catalog.filters import ItemFilter
from app_catalog.models import Item, Tag
from app_catalog.services.adding_commentary import AddingCommentaryLogin, AddingCommentaryAnonymously


class ItemList(ListView):
    model = Item
    template_name = 'catalog/catalog.html'
    paginate_by = 8
    paginate_list_range = 5
    popular_tag_amt = 5
    order_variants = {
            'popularity': 'Popularity',
            'price': 'Price',
            'commentaries': 'Commentaries',
            'created_at': 'Novelty'
        }

    def get_queryset(self):
        self.filterset = ItemFilter(self.request.GET, queryset=self.queryset)
        qs = self.filterset.qs.select_related('cover_image', 'category')
        self.queryset = qs.annotate(commentaries=Count('commentary'))
        qs = super().get_queryset()
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        # Filter context
        context['filter'] = self.filterset

        # Pagination context
        context['page_list_end'] = context['page_obj'].number + self.paginate_list_range + 1
        context['page_list_start'] = context['page_obj'].number - self.paginate_list_range - 1

        # Ordering context
        context['ordering'] = self.request.GET.get('ordering')
        context['order_variants'] = self.order_variants
        context['asc'] = self.request.GET.get('asc')

        # Popular tags context
        context['tags'] = Tag.objects.annotate(popularity=Count('item')).order_by('popularity').values('id', 'name')[:self.popular_tag_amt]

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
    model = Item
    template_name = 'catalog/product.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.prefetch_related('parameter__parameter', 'commentary').annotate(commentaries=Count('commentary'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_amt'] = self.object.commentaries
        return context


    def post(self, request, pk):
        if 'review' in request.POST:
            if request.user.id:
                adding_comment = AddingCommentaryLogin()
                adding_comment.execute(
                    text=request.POST['review'],
                    user_id=request.user.id,
                    item_id=pk,
                )
            else:
                adding_comment = AddingCommentaryAnonymously()
                adding_comment.execute(
                    text=request.POST['review'],
                    name=request.POST['name'],
                    email=request.POST['email'],
                    item_id=pk,
                )

        elif 'add-to-cart' in request.POST:
            adding_to_cart = AddingItemToCart()
            adding_to_cart.execute(pk, request.user.id, request.POST['add-to-cart'])

        return self.get(request)
