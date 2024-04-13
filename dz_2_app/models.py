from django.db import models
from django.utils import timezone


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    registration_date = models.DateField(default=timezone.now)

    def __str__(self):
        return (f'Name: {self.name}, email: {self.email}, phone: {self.phone_number}, '
                f'address: {self.address}, registration_date: {self.registration_date}')


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    add_date = models.DateField(default=timezone.now)
    photo = models.ImageField()

    def __str__(self):
        return (f'Name: {self.name}, description: {self.description}, '
                f'price: {self.price}, quantity: {self.quantity}')

    def reduce_quantity(self):
        self.quantity -= 1

    @property
    def total_quantity(self):
        return sum(product.quantity for product in Product.objects.all())


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField(default=timezone.now)

    def __str__(self):
        return (f'Client_name: {self.client}, products: {list(self.products.all())} '
                f'total_amount: {self.total_amount}, order_date: {self.order_date}')
