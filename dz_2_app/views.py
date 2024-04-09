from django.core.files.storage import FileSystemStorage
from .models import Client, Order, Product
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .forms import ProductImageForm


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


def product_image_form(request, product_id):
    if request.method == 'POST':
        form = ProductImageForm(request.POST, request.FILES)
        if form.is_valid():
            product = get_object_or_404(Product, pk=product_id)
            product_image = form.cleaned_data['product_image']
            product.photo = product_image
            product.save()
            return render(request, 'dz_2_app/image_upload.html',
            {'product': product, 'product_image': product.photo})
    else:
        form = ProductImageForm()
        return render(request, 'dz_2_app/product_image_form.html', {'form': form})
