from django.core.management.base import BaseCommand
from dz_2_app.models import Client


class Command(BaseCommand):
    help = "Create client."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Client name')
        parser.add_argument('email', type=str, help='Client email')
        parser.add_argument('phone_number', type=str, help='User phone')
        parser.add_argument('address', type=str, help='User address')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        email = kwargs.get('email')
        phone_number = kwargs.get('phone_number')
        address = kwargs.get('address')
        client = Client(name=name, email=email, phone_number=phone_number, address=address)
        client.save()
        self.stdout.write(f'{client}')
