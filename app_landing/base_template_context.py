from app_catalog.models import Category


def base_context(request):
    context = dict()

    context['user'] = request.user

    context['links'] = {
        'fb': 'https://www.facebook.com/',
        'tw': 'https://twitter.com/',
        'in': 'https://www.linkedin.com/',
        'pt': 'https://www.pinterest.ru/',
        'mail': 'mailto:mail@mail.com',
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

    context['categories'] = Category.objects.all()

    return context
