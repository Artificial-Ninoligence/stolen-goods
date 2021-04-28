from django.db import models
from django.urls import reverse


class Category(models.Model):

    slug = models.SlugField(max_length=255, unique=True)
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):

        return reverse('store:category_list', args=[self.slug])

    def __str__(self):

        return self.name
