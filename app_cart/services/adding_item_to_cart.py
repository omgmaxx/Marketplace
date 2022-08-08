class AddingItemToCart:

    def _get_cart(self, user_id):
        cart = Cart.objects.get(user=user_id)
        return cart

    def _get_item(self, item_id):
        item = Item.objects.get(id=item_id)
        return item

    def _add_position_to_cart(self, cart, item):
        position = Position.objects.get_or_create(
            cart=cart,
            item=item,
            defaults={'amount': 1}
        )
        if not position[1]: # Если позиция уже существовала
            position[0].amount += 1
            position[0].save()

    def execute(self, item_id, user_id):
        # cart = self._get_cart(user_id)
        # item = self._get_item(item_id)
        # self._add_position_to_cart(cart, item)
        print(item_id, 'is added to', user_id, 'cart')
        pass
