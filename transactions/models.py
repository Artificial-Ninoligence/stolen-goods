from django.db import models
from django.conf import settings
from product.models import Product


class Payment(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    payment_id = models.CharField(verbose_name='Payment ID', max_length=255, blank=False, null=False)
    payment_method = models.CharField(verbose_name='Payment Method', max_length=255, blank=False, null=False)
    amount_paid = models.CharField(verbose_name='Amount Paid', max_length=255, blank=False, null=False)
    status = models.CharField(verbose_name='Payment Status', max_length=255, blank=False, null=False)

    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def __str__(self):

        return self.payment_id


class Order(models.Model):

    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)

    order_number = models.CharField(verbose_name='Order Nr.', max_length=255, blank=False, null=False)
    order_note = models.CharField(verbose_name='Order Note', max_length=255, blank=True, null=True)
    order_total = models.CharField(verbose_name='Total Order', max_length=255, blank=False, null=False)
    tax = models.FloatField(verbose_name='Tax')
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip_address = models.CharField(verbose_name='IP Address', max_length=255, blank=True)
    phone_number = models.CharField(verbose_name='Phone Number', max_length=255, blank=True, null=True)
    address_line_1 = models.CharField(verbose_name='Address Line 1', max_length=255, blank=False, null=False)
    address_line_2 = models.CharField(verbose_name='address Line 2', max_length=255, blank=True, null=True)
    postal_code = models.CharField(verbose_name='Postal Code', max_length=255, blank=True, null=True)
    city = models.CharField(verbose_name='City', max_length=255, blank=True, null=True)
    state = models.CharField(verbose_name='State', max_length=255, blank=True, null=True)
    country = models.CharField(verbose_name='Country', max_length=255, blank=True, null=True)
    is_ordered = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:

        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):

        return self.user.email


class OrderProduct(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # variation = models.ForeignKey(Variation, on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='Ordered Product Quantity')
    price = models.FloatField(verbose_name='Ordered Product Price')
    is_ordered = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:

        verbose_name = 'Ordered Product'
        verbose_name_plural = 'Ordered Products'

    def __str__(self):

        return self.product.name
