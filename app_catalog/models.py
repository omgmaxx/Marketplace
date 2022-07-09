import os.path

from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name='name')

    class Meta:
        db_table = 'category'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

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


class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    short_description = models.CharField(max_length=400, verbose_name='short description')
    description = models.TextField(max_length=2000, verbose_name='description')
    price = models.PositiveIntegerField(verbose_name='price')
    created_at = models.TimeField(auto_now_add=True, verbose_name='creation date')
    edited_at = models.TimeField(auto_now=True, verbose_name='edit date')
    is_limited = models.BooleanField(verbose_name='is limited', default=False)
    is_available = models.BooleanField(verbose_name='is available', default=True)
    tags = models.ManyToManyField(Tag, related_name='item', verbose_name='tags')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='item',
                                 verbose_name='category', blank=False)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='item',
                                     verbose_name='manufacturer', blank=True, null=True)
    # delivery_types = models.ManyToManyField(DeliveryTypes, related_name='item',
    #                                         verbose_name='delivery types available')

    class Meta:
        db_table = 'item'
        verbose_name = 'item'
        verbose_name_plural = 'items'
        permissions = (
            ('change_limited', 'Can change if item is limited'),
            ('change_available', 'Can change if item is available'),
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
    created_at = models.TimeField(auto_now_add=True, verbose_name='creation date')
    edited_at = models.TimeField(auto_now=True, verbose_name='edit date')

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
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='item')
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE, verbose_name='item')
    value = models.CharField(max_length=128, verbose_name='value')

    class Meta:
        db_table = 'parameter_value'
        verbose_name = 'parameter_value'
        verbose_name_plural = 'parameter_values'
        unique_together = ('item', 'parameter')

    def __str__(self):
        return self.value


def user_directory_path(instance, filename):
    return os.path.join('item_images', instance.item.name, filename)


class Image(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='image', verbose_name='item')
    image = models.ImageField(upload_to=user_directory_path, verbose_name='image')

    class Meta:
        db_table = 'image'
        verbose_name = 'image'
        verbose_name_plural = 'images'

