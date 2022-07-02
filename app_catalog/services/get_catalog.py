from dataclasses import dataclass


@dataclass
class ItemEntity:
    pass


class GetCatalog:
    def __init__(self, filters, order_by):
        pass

    def _orm_to_entity(self, item_orm):
        # return ItemEntity(pk=item_orm.pk ... )
        pass

    def _fetch_all(self):
        # return map(self._orm_to_entity, Item.objects.filter().all())
        pass

    def _sort_by(self):
        pass

    def execute(self):
        pass
