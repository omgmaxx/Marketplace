from django.urls import reverse
from requests import request


class PaymentError(Exception):
    pass


class FictivePayment:
    """
    Validating and sending request to api

    In case of validation error returns PaymentError
    """
    def _validate_card(self, card_number: str) -> None:
        """
        Validates if card number is not odd and doesn't ends with zero
        """
        card_number = int(card_number)
        if (card_number % 2) == 1:
            raise PaymentError('Number is odd')
        if card_number % 10 == 0:
            raise PaymentError('Number ends with zero')

    def _send_to_api(self, order_id: str, card_number: str, pay_sum: str) -> None:
        """
        Sends order to API
        """
        api_url = f'{reverse("api")}/orders'
        querystring={
            'order_id': order_id,
            'card_number': card_number,
            'payment_sum': pay_sum,
        }
        request('post', url=api_url, params=querystring)

    def execute(self, order_id: str, card_number: str, pay_sum: str) -> None:
        # self._validate_card(card_number)
        # self._send_to_api(order_id, card_number, pay_sum)
        pass
