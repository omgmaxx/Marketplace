class ChangingPositionAmount:

    def _get_position(self, id):
        position = Position.objects.get(id=id)
        return position

    def _change_position_amount(self, position, operation):
        if operation == 'add':
            position.amount += 1
            position.save()

        if operation == 'sub':
            position.amount -= 1
            if position.amount > 0:
                position.save()
            else:
                position.delete()

    def execute(self, position_id, operation):
        # pos = self._get_position(position_id)
        # self._change_position_amount(pos, operation)
        pass
