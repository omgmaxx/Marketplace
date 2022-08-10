import os.path

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=64, verbose_name='name')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                            verbose_name='parent')
    is_active = models.BooleanField(default=True, verbose_name='is_active')
    icon_id = models.PositiveIntegerField(default=1, verbose_name='icon id')
    sort_index = models.IntegerField(default=0, verbose_name='sort index')

    class Meta:
        unique_together = ('name', 'parent')
        db_table = 'category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        permissions = (
            ('change_active', 'Can change if category is active'),
        )

    class MPTTMeta:
        order_insertion_by = ['sort_index']

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=64, verbose_name='name')

    class Meta:
        db_table = 'manufacturer'
        verbose_name = 'manufacturer'
        verbose_name_plural = 'manufacturers'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=64, verbose_name='name')

    class Meta:
        db_table = 'tag'
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def __str__(self):
        return self.name


class Media(models.Model):
    title = models.CharField(max_length=64, verbose_name='title')
    filename = models.CharField(max_length=64, verbose_name='file name')
    file = models.FileField(upload_to='catalog/%Y/%m/%d/', verbose_name='file', null=True, blank=True)
    link = models.URLField(verbose_name='link', blank=True)
    hash = models.CharField(max_length=32, verbose_name='hash', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creation date')

    class Meta:
        db_table = 'media'
        verbose_name = 'media'
        verbose_name_plural = 'medias'

    def __str__(self):
        return f'media/{self.file}'


class Item(models.Model):
    name = models.CharField(db_index=True, unique=True, max_length=100, verbose_name='name')
    short_description = models.TextField(max_length=400, verbose_name='short description')
    description = models.TextField(max_length=2000, verbose_name='description')
    price = models.PositiveIntegerField(verbose_name='price')
    discount = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)], verbose_name='discount in %')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creation date')
    edited_at = models.DateTimeField(auto_now=True, verbose_name='edit date')
    is_limited = models.BooleanField(verbose_name='is limited', default=False)
    is_active = models.BooleanField(verbose_name='is active', default=True)
    tags = models.ManyToManyField(Tag, related_name='item', verbose_name='tags')
    category = TreeForeignKey('Category', on_delete=models.CASCADE, related_name='items', verbose_name='category')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='item',
                                     verbose_name='manufacturer', blank=True, null=True)
    cover_image = models.ForeignKey(Media, on_delete=models.SET_NULL, related_name='covered_item', null=True,
                                    verbose_name='cover image')
    additional_image = models.ManyToManyField(Media, related_name='item', verbose_name='additional images', blank=True)
    # delivery_types = models.ManyToManyField(DeliveryTypes, related_name='item',
    #                                         verbose_name='delivery types available')

    class Meta:
        db_table = 'item'
        verbose_name = 'item'
        verbose_name_plural = 'items'
        permissions = (
            ('change_limited', 'Can change if item is limited'),
        )

    def __str__(self):
        return self.name


class Commentary(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='commentary', verbose_name='item')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commentary', verbose_name='author',
                             null=True, blank=True)
    text = models.TextField(verbose_name='text')
    name = models.CharField(max_length=32, blank=True, verbose_name='name')
    email = models.EmailField(blank=True, verbose_name='email')
    is_verified = models.BooleanField(default=True, verbose_name='is verified')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creation date')
    edited_at = models.DateTimeField(auto_now=True, verbose_name='edit date')

    class Meta:
        db_table = 'commentary'
        verbose_name = 'commentary'
        verbose_name_plural = 'commentaries'
        permissions = (
            ('change_verified', 'Can change if commentary is verified'),
        )

    def __str__(self):
        return self.text[:50]


class Parameter(models.Model):
    name = models.CharField(max_length=64, verbose_name='name')

    class Meta:
        db_table = 'parameter'
        verbose_name = 'parameter'
        verbose_name_plural = 'parameters'

    def __str__(self):
        return self.name


class ParameterValue(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='item', related_name='parameter')
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE, verbose_name='parameter', related_name='value')
    value = models.CharField(max_length=128, verbose_name='value')

    class Meta:
        db_table = 'parameter_value'
        verbose_name = 'parameter_value'
        verbose_name_plural = 'parameter_values'
        unique_together = ('item', 'parameter')

    def __str__(self):
        return f'{self.parameter.name}: {self.value}'


class Retailer(models.Model):
    name = models.CharField(max_length=128, verbose_name='name')
    address = models.CharField(max_length=128, verbose_name='address')

    class Meta:
        db_table = 'retailer'
        verbose_name = 'retailer'
        verbose_name_plural = 'retailers'

    def __str__(self):
        return f'{self.name} at {self.address}'


class RetailerAvailability(models.Model):
    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE, related_name='availability',
                                 verbose_name='retailer')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='availability',
                             verbose_name='item')
    is_available = models.BooleanField(default=True, verbose_name='is available')
    edited_at = models.DateTimeField(auto_now=True, verbose_name='edit date')

    class Meta:
        unique_together = ('retailer', 'item')
        db_table = 'availability'
        verbose_name = 'availability'
        verbose_name_plural = 'available at'
        permissions = (
            ('change_availability', 'Can change availability'),
        )

    def __str__(self):
        return f'{self.item} is {("" if self.is_available else "not")} available at {self.retailer}'
