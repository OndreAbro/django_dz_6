from django.core.management.base import BaseCommand
from dz_2_app.models import Order, Client, Product


class Command(BaseCommand):
    help = "Get all orders by client id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client id')

    def handle(self, *args, **kwargs):
        client = Client.objects.filter(pk=kwargs.get('pk')).first()
        if client:
            orders = Order.objects.filter(client=client)
            intro = f'All orders of {client.name}\n'
            text = '\n'.join([str(order) for order in orders])
            self.stdout.write(f'{intro}{text}')
