from django.test import TestCase
from product.models import Product


class ProductTest(TestCase):

    def setUp(self):

        self.product = Product.objects.create(
            category='Jewellery',
            created_by='User',
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
