from django.core.management.base import BaseCommand
from dz_2_app.models import Order, Client, Product


class Command(BaseCommand):
    help = "Create order."

    def add_arguments(self, parser):
        parser.add_argument('client', type=int, help='Client id')
        parser.add_argument('products', type=str, help='Product list')

    def handle(self, *args, **kwargs):
        client = Client.objects.get(pk=kwargs.get('client'))
        products = list(Product.objects.filter(pk=product).first() for product in kwargs.get('products').split(','))
        total_amount = sum((product.price for product in products))
        order = Order(client=client, total_amount=total_amount)
        order.save()
        for product in products:
            product.reduce_quantity()
            product.save()
            order.products.add(product)
        self.stdout.write(f'{order}')
