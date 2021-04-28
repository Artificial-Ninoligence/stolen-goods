from category.models import Category
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings



class Product(models.Model):

    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='product_owner', on_delete=models.CASCADE)

    slug = models.SlugField(max_length=255, blank=False, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, blank=False, null=False)
    stock = models.IntegerField(default=1)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('-created_at',)

    def empty_stock(self, stock):

        if stock == 0:
            self.in_stock = False

    def __str__(self):

        return self.name