class RemovingItemFromCart:

    def _get_position(self, id):
        position = Position.objects.get(id=id)
        return position

    def _sub_position_from_cart(self, position):
        position.delete()

    def execute(self, position_id):
        # pos = self._get_position(position_id)
        # self._sub_position_from_cart(pos)
        pass
