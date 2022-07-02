from dataclasses import dataclass


@dataclass
class PurchaseEntity:
    pass


class GetHistory:
    def __init__(self, cart_id):
        pass

    def _orm_to_entity(self, purchase_orm):
        # return PurchaseEntity(pk=purchase_orm.pk ... )
        pass

    def _fetch_all(self):
        # return map(self._orm_to_entity, PurchaseHistory.objects.filter().all())
        pass

    def execute(self):
        pass