from django.test import TestCase
from product.models import Product
from category.models import Category
from django.contrib.auth.models import User


class ProductTest(TestCase):

    def setUp(self):

        user = User.objects.create(
            username='User',
            email='user@test.com',
            password='foo'
        )

        category = Category.objects.create(
            name='Jewellery',
            slug='jewellery'
        )

        self.product = Product.objects.create(
            category=category,
            owner=user,
            slug='napoleon-crown',
            name='Napoleon Crown',
            description='Crown used by Napoleon Bonaparte',
            price=50000000000,
            image='Crown.png',
            stock=1,
            in_stock=True,
            is_active=True,
            )

    def test_create_product(self):

        product = self.product

        self.assertIsInstance(product, Product)
