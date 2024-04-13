from django.urls import path
from .views import client_products, product_image_form
from .views import total_in_db, total_in_view, total_in_template

urlpatterns = [
    path('client/<int:client_id>/', client_products, name='client_products'),
    path('product/<int:product_id>/add/', product_image_form, name='product_image_form'),
    path('db/', total_in_db, name='db'),
    path('view/', total_in_view, name='view'),
    path('template/', total_in_template, name='template'),
]
