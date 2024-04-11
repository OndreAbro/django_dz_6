from django.contrib import admin
from .models import Client, Product, Order


@admin.action(description='Сбросить количество в ноль')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'address', 'registration_date']
    ordering = ['name', 'registration_date', 'address']
    list_filter = ['name', 'address']
    search_fields = ['name', 'email', 'address']
    fields = ['name', 'email', 'phone_number', 'address', 'registration_date']
    readonly_fields = ['registration_date']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'add_date']
    ordering = ['add_date', '-quantity']
    list_filter = ['add_date', 'price']
    search_fields = ['description']
    actions = [reset_quantity]
    fields = ['name', 'description', 'add_date', 'quantity', 'photo']
    readonly_fields = ['add_date', 'quantity']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'total_amount', 'order_date']
    ordering = ['client', '-total_amount']
    list_filter = ['order_date', 'total_amount']
    search_fields = ['client', 'products']
    fields = ['client', 'products', 'order_date', 'total_amount']
    readonly_fields = ['client', 'products', 'order_date', 'total_amount']

    def has_add_permission(self, request):
        return False


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
