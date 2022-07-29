from django.db.models import Sum, F


class GetCartDiscount:

    def _get_cart(self, user_id):
        cart = Cart.objects.get(user=user_id)
        return cart

    def _get_total_discount(self, cart):
        # Возможно, часть расчётов перекинется на "get_cart_total_price"
        total_discount = cart.position.objects.aggregate(
            total=Sum(F('amount') * F('item__price') * F('item__discount'))
        )['total']
        return total_discount

    def execute(self, user_id):
        # cart = self._get_cart(user_id)
        # total_discount = self._get_total_discount(cart)

        total_discount = 5999 # заглушка
        return total_discount
