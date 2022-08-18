from django.db.models import Count
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from app_cart.services.adding_item_to_cart import AddingItemToCart
from app_catalog.filters import ItemFilter
from app_catalog.forms import CommentForm
from app_catalog.models import Item, Tag
from app_catalog.services.adding_commentary import AddingCommentary
from app_catalog.services.get_comment_amount_of_item import GetCommentAmountOfItem
from app_catalog.services.get_comments_of_item import GetCommentsOfItem
from app_catalog.services.get_medias_of_item import GetMediasOfItem


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


class ItemDetail(FormMixin, DetailView):
    model = Item
    template_name = 'catalog/product.html'
    form_class = CommentForm

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.prefetch_related('parameter__parameter', 'commentary', 'commentary__user', 'cover_image', 'additional_image'
                                         ).annotate(commentary_amt=Count('commentary'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['comment_amt'] = GetCommentAmountOfItem().execute(self.object)
        context['commentaries'] = GetCommentsOfItem().execute(self.object)

        cover_image, additional_pics = GetMediasOfItem().execute(self.object)
        context['cover_image'] = cover_image
        context['additional_pics'] = additional_pics

        return context

    def get_success_url(self):
        return reverse('catalog-item', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        adding_comment = AddingCommentary()
        adding_comment.execute(
            text=form.cleaned_data.get('review'),
            user_id=self.request.user.id,
            item_id=self.get_object().pk,
            name=form.cleaned_data.get('name'),
            email=form.cleaned_data.get('email'),
        )
        return super().form_valid(form)

    def post(self, request, pk, *args, **kwargs):
        self.object = self.get_object()

        if 'review' in request.POST:
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)

        if 'add-to-cart' in request.POST:
            adding_to_cart = AddingItemToCart()
            adding_to_cart.execute(pk, request.user.id, request.POST['add-to-cart'])
            return HttpResponseRedirect(self.get_success_url())

