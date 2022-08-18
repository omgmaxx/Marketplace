class GetCommentAmountOfItem:

    def _get_comment_amount(self, item):
        commentary_amt = item.commentary_amt
        return commentary_amt

    def execute(self, item):
        commentary_amt = self._get_comment_amount(item)
        return commentary_amt
