from django.urls import path

from views import Cart

urlpatterns = [
    path('', Cart.as_view(), name='cart'),
]