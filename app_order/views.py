from django.views.generic import CreateView, UpdateView, TemplateView


class CreateOrder(CreateView):
    # fields = []
    pass


class OrderDeliveryType(UpdateView):
    # fields = []
    pass


class OrderPaymentType(UpdateView):
    # fields = []
    pass


class OrderConfirmation(TemplateView):

    def post(self, request):
        pass


class OrderPayment(TemplateView):

    def post(self, request):
        pass
