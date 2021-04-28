from django.contrib import admin
from .models import Payment, Order, OrderProduct


class PaymentAdmin(admin.ModelAdmin):

    list_display = ('payment_id', 'amount_paid', 'payment_method', 'status', 'date_created',)
    list_filter = ('status', 'payment_id', 'date_created',)
    fieldsets = (
        (None, {'classes': ('wide', 'extrapretty'),
                'fields': ('payment_id',)}),
        ('Payment Details', {'fields': ('user', 'amount_paid', 'status', 'payment_method',)}),
    )


class OrderAdmin(admin.ModelAdmin):

    list_display = ('order_number', 'order_total', 'status', 'tax', 'is_ordered', 'date_created', 'date_updated',)
    list_filter = ('order_number', 'status', 'is_ordered', 'date_updated', 'date_created',)
    fieldsets = (
        (None, {'classes': ('wide', 'extrapretty'),
                'fields': ('order_number', 'user', 'payment',)}),
        ('Order Details', {'fields': (
            'order_total',
            'order_note',
            'status',
            'tax',
            'is_ordered',
            )}),
        ('Address Details', {'fields': (
            'address_line_1',
            'address_line_2',
            'phone_number',
            'postal_code',
            'city',
            'state',
            'country',
            )}),
    )


class OrderItemAdmin(admin.ModelAdmin):

    list_display = ('quantity', 'price', 'is_ordered', 'date_created', 'date_updated',)
    list_filter = ('is_ordered', 'quantity', 'date_created', 'date_updated',)
    fieldsets = (
        (None, {'classes': ('wide', 'extrapretty'),
                'fields': ('price', 'quantity', 'is_ordered',)}),
    )


admin.site.register(Payment, PaymentAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderItemAdmin)
