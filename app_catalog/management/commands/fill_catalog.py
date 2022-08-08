import random
from random import randint

from django.core.management import BaseCommand

from app_catalog.models import Item, Tag, Category, Manufacturer, Media



class Command(BaseCommand):
    help = 'fills app_catalog db'

    def handle(self, *args, **options):
        tags = Tag.objects.all()
        categories = Category.objects.all()
        manufacturers = Manufacturer.objects.all()
        cover_image = Media.objects.get(id=6)

        for object_id in range(500):
            obj = Item.objects.get_or_create(id=object_id, defaults={
                'name': f'object{object_id}',
                'short_description': [object_id for _ in range(50)],
                'description': [object_id for _ in range(150)],
                'price': randint(50, 5000),
                'discount': 0 if randint(0, 100) < 80 else 25,
                'is_limited': random.choice((True, False)),
                'is_active': random.choice((True, False)),
                'category': random.choice(categories),
                'manufacturer': random.choice(manufacturers),
                'cover_image': cover_image,
            })
            if obj[1]:
                obj[0].tags.set({random.choice(tags), random.choice(tags), random.choice(tags)})
