from django.utils.safestring import mark_safe
from django.views.generic import TemplateView


class MainPage(TemplateView):
    template_name = 'landing/main.html'

    def get_context_data(self, **kwargs):
        context = super(MainPage, self).get_context_data(**kwargs)

        context['user'] = self.request.user

        context['links'] = {
            'fb': 'https://www.facebook.com/',
            'tw': 'https://twitter.com/',
            'in': 'https://www.linkedin.com/',
            'pt': 'https://www.pinterest.ru/',
            'mail': 'mail@mail.com',
        }

        context['cart'] = {
            'amt': 5,
            'price': 5.25,
        }

        context['contacts'] = {
            'phone': f'{8800200600:,}'.replace(',', '.'),
            'email': 'Support@ninzio.com',
            'skype': 'techno',
            'address': ['New York, north', 'Avenue 26/7', '0057'],
        }

        # здесь будет кэширование

        return context
