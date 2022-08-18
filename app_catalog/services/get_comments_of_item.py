from app_catalog.models import Commentary


class GetCommentsOfItem:
    def _get_comment_list(self, item):
        return item.commentary.all()

    def execute(self, item):
        commentary_list = self._get_comment_list(item)

        return commentary_list


