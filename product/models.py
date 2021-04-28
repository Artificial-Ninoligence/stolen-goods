from category.models import Category
from django.db import models
from django.conf import settings
from django.urls import reverse
from victim.models import Victim
from django.db.models import Avg, Count


class Product(models.Model):

    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='product_owner', on_delete=models.CASCADE)
    victim = models.ForeignKey(Victim, on_delete=models.DO_NOTHING, blank=True, null=True)

    slug = models.SlugField(max_length=255, blank=False, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, blank=False, null=False)
    stock = models.IntegerField(default=1)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('-created_at',)

    def empty_stock(self, stock):

        if stock == 0:
            self.in_stock = False

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def averageReview(self):
        reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg

    def countReview(self):
        reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count

    def __str__(self):

        return self.name


class ReviewRating(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    subject = models.CharField(verbose_name='Subject', max_length=100, blank=True, null=True)
    review = models.TextField(verbose_name='Review Text', blank=True, null=True)
    rating = models.FloatField(verbose_name='Rating')
    ip_address = models.CharField(verbose_name='IP Address', max_length=500, blank=True, null=True)
    status = models.BooleanField(default=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:

        verbose_name = 'Review & Rating'
        verbose_name_plural = 'Reviews & Ratings'

    def __str__(self):

        return self.subject


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images', max_length=255)

    class Meta:
        verbose_name = 'Product Gallery'
        verbose_name_plural = 'Product Galleries'

    def __str__(self):
        return self.product.name
