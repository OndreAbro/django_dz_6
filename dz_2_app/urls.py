from django.urls import path
from .views import client_products, product_image_form

urlpatterns = [
    path('client/<int:client_id>/', client_products, name='client_products'),
    path('product/<int:product_id>/add/', product_image_form, name='product_image_form'),
]
