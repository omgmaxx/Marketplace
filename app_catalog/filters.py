from decimal import Decimal

from django.db.models import Max
from django.forms import TextInput
from django_filters import RangeFilter, CharFilter, ModelChoiceFilter, ModelMultipleChoiceFilter, \
    FilterSet, BooleanFilter
from django_filters.widgets import BooleanWidget
from django.utils.translation import gettext as _

from app_catalog.models import Item, Manufacturer, Tag, Category


class CustomTextInput(TextInput):
    # Added saving value to field
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['attrs']['data-max'] = Item.objects.aggregate(Max('price'))['price__max']
        if value:
            value = value.split(';')
            context['widget']['attrs']['data-from'] = value[0]
            context['widget']['attrs']['data-to'] = value[1]
        return context


class CBooleanWidget(BooleanWidget):
    # Cleaning boolean fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.choices = (("", _("")), ("true", _("Yes")), ("false", _("No")))


class ItemFilter(FilterSet):
    price = RangeFilter(field_name='price',
                        widget=CustomTextInput(attrs={
                            'class': 'range-line',
                            'data-type': "double",
                            'data-min': "0",
                            'data-max': "1000",
                            'data-from': "0",
                            'data-to': "500000",
                        }))

    name = CharFilter(field_name='name', label='Name', lookup_expr='icontains')
    is_limited = BooleanFilter(field_name='is_limited', label='Limited', widget=CBooleanWidget())
    available = BooleanFilter(field_name='availability__is_available', label='Available', widget=CBooleanWidget())
    manufacturer = ModelChoiceFilter(field_name='manufacturer', label='Manufacturer', queryset=Manufacturer.objects.all())
    tags = ModelMultipleChoiceFilter(field_name='tags', label='Tags', queryset=Tag.objects.all(), conjoined=True)
    category = ModelChoiceFilter(field_name='category', label='Category', queryset=Category.objects.all())

    class Meta:
        model = Item
        fields = ['price', 'name', 'is_limited', 'available', 'manufacturer', 'tags', 'category']

    def price_appoint(self, queryset):
        """
        Filters queryset with value of <input> with name="price"
        """

        value = self.data.get('price')
        if value:
            value = value.split(';')
            return self.filters['price'].filter(queryset, slice(Decimal(value[0]), Decimal(value[1]), None))
        return queryset

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        queryset = self.price_appoint(queryset)
        return queryset
