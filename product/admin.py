from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):

    list_display = ['slug', 'name', 'price', 'stock', 'in_stock', 'is_active', 'created_at', 'updated_at']
    list_filter = ['in_stock', 'is_active', 'created_at']
    list_editable = ['in_stock', 'in_stock']
    prepopulated_field = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)
