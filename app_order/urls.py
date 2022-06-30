from django.urls import path

from views import CreateOrder, OrderConfirmation, OrderPaymentType, OrderDeliveryType, OrderPayment

urlpatterns = [
    path('', CreateOrder.as_view(), name='make-order'),
    path('delivery/', OrderDeliveryType.as_view(), name='delivery'),
    path('paymenttype/', OrderPaymentType.as_view(), name='payment-type'),
    path('confirmation/', OrderConfirmation.as_view(), name='confirmation'),
    path('payment/', OrderPayment.as_view(), name='payment'),
]