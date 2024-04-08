from .models import Client, Order, Product
from django.shortcuts import render, get_object_or_404
from datetime import datetime


def client_products(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client=client).order_by('-id')
    products_week = []
    products_month = []
    products_year = []
    for order in orders:
        if (datetime.date(datetime.now()) - order.order_date).days < 2:
            products_week.append(order.products.all())
        elif (datetime.date(datetime.now()) - order.order_date).days < 30:
            products_month.append(order.products.all())
        elif (datetime.date(datetime.now()) - order.order_date).days < 365:
            products_year.append(order.products.all())
    return render(request, 'dz_2_app/client_products.html',
                  {'client': client,
                   'products_week': products_week,
                   'products_month': products_month,
                   'products_year': products_year,
                   })
