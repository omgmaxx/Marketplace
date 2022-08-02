import logging

from django.db.models import Sum

from app_order.services.fictive_payment import FictivePayment, PaymentError

logger = logging.getLogger(__name__)


class PayForOrder:
    """
    Attempts to make payment for order
    """

    def _get_order(self, order_id: str):
        """
        Gets order from DB
        """
        order = Order.objects.get(id=order_id)
        return order

    def _get_total_sum(self, order: Order):
        """
        Gets total price of all items in order
        """
        total_sum = order.items.aggregate[Sum('price')]
        return total_sum

    def _try_to_pay(self, order_id: str, card_num: str, total_sum: str, order: Order) -> str:
        """
        Attempts to execute FictivePayment and gives "finished" status

        In case of error sends it to logger and gives "failed" status
        """
        try:
            fic_pay = FictivePayment()
            fic_pay.execute(order_id, card_num, total_sum)
            order.status = Status.objects.get(name='Finished')
        except PaymentError as e:
            logger.error(e)
            order.status = Status.objects.get(name='Failed')
        finally:
            order.save(update_fields=['status'])
            return order.status

    def execute(self, order_id: str) -> str:
        # order = self._get_order(order_id)
        # total_sum = self._get_total_sum(order)
        # status = self._try_to_pay(order_id, order['card_num'], total_sum, order)
        # return status

        return 'Finished' # Заглушка


    