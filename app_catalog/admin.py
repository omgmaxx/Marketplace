from django.contrib import admin
from .models import Category, Manufacturer, Item, Commentary, Image, Tag, Parameter, ParameterValue


class CommentaryInline(admin.StackedInline):
    model = Commentary
    readonly_fields = ('text', 'user', 'name')
    fields = ('text', 'user', 'name', 'is_verified', )
    extra = 0


class ImageInline(admin.StackedInline):
    model = Image
    verbose_name = 'image'
    verbose_name_plural = 'images'
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


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
    pass


class ParameterValueInline(admin.StackedInline):
    model = ParameterValue
    fields = ('parameter', 'value')
    verbose_name = 'parameter'
    verbose_name_plural = 'parameters'
    extra = 0


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_limited', 'is_available', 'category', 'manufacturer']
    fields = ['name', 'short_description', 'description', 'price', 'is_limited', 'is_available', 'category', 'manufacturer', 'tags']
    list_filter = ['is_limited', 'is_available', 'category', 'manufacturer', 'tags']
    inlines = [CommentaryInline, ImageInline, ParameterValueInline]


