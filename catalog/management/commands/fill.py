from datetime import datetime
from random import randint

from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        product_list = [{'product_name': 'Картофель', 'product_description': 'картошка',
                         'product_category': 'овощи',
                         'product_price': randint(50, 150), 'create_date': datetime.now()},
                        {'product_name': 'Томаты', 'product_description': 'помидоры',
                         'product_category': 'овощи',
                         'product_price': randint(50, 150), 'create_date': datetime.now()},
                        {'product_name': 'Капуста', 'product_description': 'качан',
                         'product_category': 'овощи',
                         'product_price': randint(50, 150), 'create_date': datetime.now()},
                        {'product_name': 'Огурцы', 'product_description': 'длинные',
                         'product_category': 'овощи',
                         'product_price': randint(50, 150), 'create_date': datetime.now()},
                        ]
        products_for_create = []
        Product.objects.all().delete()
        for product in product_list:
            products_for_create.append(Product(**product))
        Product.objects.bulk_create(products_for_create)
