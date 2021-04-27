from django.test import TestCase
from category.models import Category


class CategoryTest(TestCase):

    def test_create_category(self):

        category = Category.objects.create(name='Jewellery', slug='jewellery')

        self.assertIsInstance(category, Category)
