from django.test import TestCase
from category.models import Category


class TestCategory(TestCase):

    def setUp(self):

        self.category = Category.objects.create(name='Jewellery', slug='jewellery')

    def test_category_model_entry(self):

        category = self.category

        self.assertIsInstance(category, Category)
