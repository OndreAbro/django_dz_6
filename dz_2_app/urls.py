from django.urls import path
from .views import client_products

urlpatterns = [
    path('client/<int:client_id>/', client_products, name='client_products'),
]
