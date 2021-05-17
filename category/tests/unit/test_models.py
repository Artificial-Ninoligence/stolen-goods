from django.test import TestCase
from category.models import Category


class TestCategory(TestCase):

    def setUp(self):

        self.category = Category.objects.create(
            name='Jewellery',
            slug='jewellery',
            description='Oldest artefact used to show status',
            image='jewellery.png',
        )

    def test_category_model_entry(self):

        category = self.category

        self.assertTrue(isinstance(category, Category))
        self.assertEqual(str(category), 'Jewellery')
