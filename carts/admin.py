from django.contrib import admin
from .models import Cart, CartItem


class CartAdmin(admin.ModelAdmin):

    list_display = ('cart_id', 'date_added',)
    list_filter = ('cart_id', 'date_added',)
    fieldsets = (
        (None, {'classes': ('wide', 'extrapretty'),
                'fields': ('cart_id',)}),
    )


class CartItemAdmin(admin.ModelAdmin):

    list_display = ('quantity', 'is_active',)
    list_filter = ('quantity', 'is_active',)
    fieldsets = (
        (None, {'classes': ('wide', 'extrapretty'),
                'fields': ('cart', 'product', 'quantity', 'is_active',)}),
    )


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)