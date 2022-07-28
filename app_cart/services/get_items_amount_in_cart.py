from django.db.models import Sum


class GetItemAmountInCart:

    def _get_cart(self, user_id):
        cart = Cart.objects.get(user=user_id)
        return cart

    def _get_items_amount(self, cart):
        total_amount = cart.position.aggregate(Sum('amount'))
        return total_amount


    def execute(self, user_id):
        # cart = self._get_cart(user_id)
        # total_amount = self._get_items_amount(cart)

        total_amount = 50 # заглушка
        return total_amount
