from django.contrib.auth.models import User
from django.db import models

from app_catalog.models import Media


class UserMedia(Media):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_media', verbose_name='uploader')
    is_verified = models.BooleanField(default=True, verbose_name='is verified')


    class Meta:
        db_table = 'user_media'
        verbose_name = 'user_media'
        verbose_name_plural = 'user_medias'
        permissions = (
            ('change_verified', 'Can change if user media is verified'),
        )

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='user')
    avatar = models.ForeignKey(UserMedia, on_delete=models.SET_NULL, blank=True, null=True, related_name='profile',
                               verbose_name='avatar')
    middle_name = models.CharField(max_length=50, blank=True, verbose_name='middle name')
    phone_number = models.CharField(max_length=16, blank=True, verbose_name='phone number')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creation date')
    edited_at = models.DateTimeField(auto_now=True, verbose_name='edit date')

    class Meta:
        db_table = 'profile'
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
        permissions = (
            ('change_active', 'Can change if user is active'),
        )

    def __str__(self):
        return f"{self.user.username}'s profile"
