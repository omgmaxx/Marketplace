from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from .models import Category, Manufacturer, Item, Commentary, Media, Tag, Parameter, ParameterValue, \
    Retailer, RetailerAvailability


class CommentaryInline(admin.StackedInline):
    model = Commentary
    # readonly_fields = ('text', 'user', 'name', 'email')
    readonly_fields = ('edited_at', 'created_at')
    fields = ('text', 'user', 'name', 'email', 'is_verified', 'edited_at', 'created_at')
    extra = 0
    can_delete = False


class RetailerAvailabilityInline(admin.TabularInline):
    model = RetailerAvailability
    readonly_fields = ('edited_at', )
    fields = ('item', 'retailer', 'is_available', 'edited_at')
    extra = 0
    can_delete = False


class ParameterValueInline(admin.TabularInline):
    model = ParameterValue
    fields = ('parameter', 'value')
    extra = 0


@admin.register(Category)
class CategoryAdmin(DjangoMpttAdmin):
    list_filter = ('is_active', )


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    pass


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ['get_text', 'user', 'name', 'is_verified', 'item']

    def get_text(self, obj):
        return obj.text[:50]
    get_text.short_description = 'text'


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    pass


@admin.register(Retailer)
class RetailerAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
    inlines = [RetailerAvailabilityInline, ]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_limited', 'is_active', 'category', 'manufacturer', 'get_tags', 'get_available_retailers']
    list_filter = ['is_limited', 'category', 'manufacturer', 'tags']
    inlines = [ParameterValueInline, RetailerAvailabilityInline, CommentaryInline]

    def get_tags(self, obj):
        return list(obj.tags.all())
    get_tags.short_description = 'tags'

    def get_available_retailers(self, obj):
        return list({ret.retailer.name for ret in obj.availability.prefetch_related('retailer').filter(is_available=True)})
    get_available_retailers.short_description = 'available retailers'
