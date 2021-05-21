from django.test import TestCase
from product.models import Product, ReviewRating
from category.models import Category
from django.contrib.auth import get_user_model


CustomUser = get_user_model()
class TestProduct(TestCase):

    def setUp(self):

        category = Category.objects.create(
            name='Jewellery',
            slug='jewellery',
            description='Oldest artefact used to show status',
            image='jewellery.png',
        )

        self.product = Product.objects.create(
            category_id=1,
            slug='blue-ocean-necklace',
            name='Blue Ocean Necklace',
            price=300000000,
            discounted_price=10000,
        )

    def test_product_creation(self):

        test_product = self.product

        self.assertTrue(isinstance(test_product, Product))
        self.assertTrue(test_product.is_available, True)
        self.assertEqual(test_product.stock, 1)
        self.assertEqual(test_product.image, 'product_images/main_photo/default-product.png')
        self.assertEqual(test_product.description, None)
        self.assertEqual(test_product.get_url(), f"/category/{test_product.category.slug}/{test_product.slug}/")
        self.assertEqual(test_product.__str__(), test_product.name)
