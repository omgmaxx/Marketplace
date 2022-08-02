class GetOrderStatus:
    """
    Returns order status
    """

    def _get_order(self, order_id: str) -> Order:
        """
        Gets order by ID
        """

        order = Order.objects.get(user=order_id)
        return order

    def _get_order_status(self, order: Order) -> str:
        """
        Gets order's status
        """

        status = order.status
        return status

    def execute(self, order_id: str) -> str:
        order = self._get_order(order_id)
        status = self._get_order_status(order)

        status = "Finished" # заглушка
        return status
