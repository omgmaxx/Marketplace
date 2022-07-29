from django.db.models import Sum


class GetCommentAmountOfItem:

    def _get_item(self, item_id):
        item = Item.objects.get(id=item_id)
        return item

    def _get_comment_amount(self, item):
        commentary_amt = item.commentary.aggregate(Sum('amount'))
        return commentary_amt

    def execute(self, item_id):
        # item = self._get_item(item_id)
        # commentary_amt = self._get_comment_amount(item)

        commentary_amt = 15 # заглушка
        return commentary_amt
