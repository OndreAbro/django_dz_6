from django.core.management.base import BaseCommand
from dz_2_app.models import Client


class Command(BaseCommand):
    help = "Update client name by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('name', type=str, help='Client name')
        parser.add_argument('email', type=str, help='Client email')
        parser.add_argument('phone_number', type=str, help='User phone')
        parser.add_argument('address', type=str, help='User address')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        email = kwargs.get('email')
        phone_number = kwargs.get('phone_number')
        address = kwargs.get('address')
        client = Client.objects.filter(pk=pk).first()
        client.name = name
        client.email = email
        client.phone_number = phone_number
        client.address = address
        client.save()
        self.stdout.write(f'{client}')
