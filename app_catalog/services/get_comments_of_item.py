class GetCommentsOfItem:

    def _get_item(self, item_id):
        item = Item.objects.get(id=item_id)
        return item

    def _get_comment_list(self, item):
        return (comment for comment in item.commentary.all())

    def execute(self, item_id):
        # item = self._get_item(item_id)
        # commentary_list = self._get_comment_list(item)

        commentary_list = (1, 2, 3) # заглушка
        return commentary_list


