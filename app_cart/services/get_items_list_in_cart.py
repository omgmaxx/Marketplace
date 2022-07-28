class GetItemListInCart:

    def _get_cart(self, user_id):
        cart = Cart.objects.get(user=user_id)
        return cart

    def _get_item_list(self, cart):
        return (pos.item for pos in cart.position.all())

    def execute(self, user_id):
        # cart = self._get_cart(user_id)
        # i_list = self._get_item_list(cart)

        i_list = (0, 1, 2) # заглушка
        return i_list


