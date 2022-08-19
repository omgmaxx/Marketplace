from django.db.models import Min, Count
from django.views.generic import ListView

from app_catalog.models import Item, Category


class MainPage(ListView):
    template_name = 'landing/main.html'
    model = Item

    def get_queryset(self):
        queryset = super(MainPage, self).get_queryset().select_related('category', 'cover_image'
                                                                       ).annotate(commentaries=Count('commentary'))
        return queryset

    def filter_limited(self):
        queryset = self.get_queryset()
        queryset = queryset.filter(is_limited=True)
        return queryset[:8]

    def filter_popular(self):
        queryset = self.get_queryset()
        # Ordering placeholder
        return queryset[:8]

    def get_popular_categories(self):
        queryset = Category.objects.all()
        queryset = queryset.annotate(min_price=Min('items__price'))
        return queryset[:3]


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MainPage, self).get_context_data(**kwargs)

        context['popular_categories'] = self.get_popular_categories()
        context['limited_list'] = self.filter_limited()
        context['popular_list'] = self.filter_popular()

        return context
