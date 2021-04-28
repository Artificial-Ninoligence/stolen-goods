from django.test import TestCase
from product.models import Product
from category.models import Category
from django.contrib.auth import get_user_model

User = get_user_model()


class TestProduct(TestCase):

    def setUp(self):

        User.objects.create(username='Admin')

        Category.objects.create(name='Jewellery', slug='jewellery')

        self.product = Product.objects.create(
            category_id=1,
            owner_id=1,
            slug='napoleon-crown',
            name='Napoleon Crown',
            description='Crown used by Napoleon Bonaparte',
            price=50000000000,
            image='Crown.png',
            stock=1,
            is_available=True,
            )

    def test_product_model_entry(self):

        product = self.product

        self.assertTrue(isinstance(product, Product))
        self.assertEqual(str(product), 'Napoleon Crown')
