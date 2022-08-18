from django.contrib.auth.models import User

from app_catalog.models import Commentary, Item


class AddingCommentary:
    def _get_item(self, item_id):
        item = Item.objects.get(id=item_id)
        return item

    def _get_user(self, user_id):
        user = User.objects.get(id=user_id)
        return user

    def _create_commentary_login(self, user, item, text):
        commentary = Commentary.objects.create(
            user=user,
            item=item,
            is_verified=True,
            text=text
        )
        return commentary

    def _create_commentary_anon(self, text, item, email, name):
        commentary = Commentary.objects.create(
            item=item,
            name=name,
            email=email,
            is_verified=True,
            text=text
        )
        return commentary

    def execute(self, text, item_id, name, email, user_id=None):
        item = self._get_item(item_id)
        if not user_id:
            if not name:
                name = 'Anonymous'
            comment = self._create_commentary_anon(text=text, item=item, email=email, name=name)
        else:
            user = self._get_user(user_id)
            comment = self._create_commentary_login(text=text, user=user, item=item)
        return comment
