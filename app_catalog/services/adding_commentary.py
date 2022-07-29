from django.contrib.auth.models import User


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
            verified=True,
            text=text
        )
        return commentary

    def _create_commentary_anon(self, name, email, text):
        commentary = Commentary.objects.create(
            name=name,
            email=email,
            verified=True,
            text=text
        )
        return commentary

    def execute(self, user_id, text, item_id=None, name='Anonymous', email=''):
        # item = self._get_item(item_id)
        #
        # # Is registered user?
        # if item_id:
        #     user = self._get_user(user_id)
        #     comment = self._add_commentary_to_item_login(user, item, text)
        # else:
        #     comment = self._add_commentary_to_item_anon(name, email, text)

        comment = 1 # заглушка
        return comment
