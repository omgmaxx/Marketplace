from django.contrib.auth.models import User

from app_catalog.models import Commentary, Item


class AddingCommentary:

    def _get_item(self, item_id):
        item = Item.objects.get(id=item_id)
        return item

    def _get_user(self, user_id):
        user = User.objects.get(id=user_id)
        return user


class AddingCommentaryAnonymously(AddingCommentary):
    def _create_commentary(self, name, item, email, text):
        commentary = Commentary.objects.create(
            item=item,
            name=name,
            email=email,
            is_verified=True,
            text=text
        )
        return commentary

    def execute(self, text, item_id, name, email):
        if not name:
            name = 'Anonymous'
        item = self._get_item(item_id)
        comment = self._create_commentary(name, item, email, text)
        return comment


class AddingCommentaryLogin(AddingCommentary):
    def _create_commentary(self, user, item, text):
        commentary = Commentary.objects.create(
            user=user,
            item=item,
            is_verified=True,
            text=text
        )
        return commentary

    def execute(self, user_id, item_id, text):
        item = self._get_item(item_id)
        user = self._get_user(user_id)
        comment = self._create_commentary(user, item, text)
        return comment