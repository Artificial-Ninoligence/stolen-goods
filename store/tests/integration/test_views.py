# import pytest
from django.test import TestCase, Client
from django.urls import reverse
from category.models import Category
from product.models import Product
from store.views import home, store, product_detail, submit_review


class TestStoreView(TestCase):

    def setUp(self):

        self.category_1 = Category.objects.create(
            name='Jewellery',
            slug='jewellery',
            description='Oldest artefact used to show status',
            image='jewellery.png',
        )

        self.category_2 = Category.objects.create(
            name='Art',
            slug='art',
            description='Creative masterpiece',
            image='art.png',
        )

        self.product_1 = Product.objects.create(
            category_id=1,
            slug='blue-ocean-necklace',
            name='Blue Ocean Necklace',
            price=300000000,
        )

        self.product_2 = Product.objects.create(
            category_id=1,
            slug='pink-panther-diamond',
            name='Pink Panther Diamond',
            price=900000000,
        )

        client = Client()
        self.home_response = client.get('/')
        self.store_response = client.get('/store/')

        # Product.get_url() return reverse('product-detail', kwargs=[category_id.slug, Product.slug])
        self.product_1_detail_response = client.get(self.product_1.get_url())
        self.product_2_detail_response = client.get(self.product_2.get_url())

    def test_home_template_and_url_status_code_200(self):

        response = self.home_response
        test_categories = [self.category_1, self.category_2]
        test_products = [self.product_1, self.product_2]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.func, home)
        self.assertEqual(
            str(response.context['categories']),
            f"<QuerySet [<Category: {test_categories[0].name}>, <Category: {test_categories[1].name}>]>"
        )

        # By default, all products are created and appended by descending order based on its index: '-date_created'
        self.assertEqual(
            str(response.context['products']),
            f"<QuerySet [<Product: {test_products[1].name}>, <Product: {test_products[0].name}>]>")

    def test_store_template_and_url_status_code_200(self):

        response = self.store_response

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.func, store)
        self.assertEqual(str(response.context['products']), '<Page 1 of 1>')
        self.assertEqual(response.context['product_count'], 2)

    def test_product_detail_template_and_url_status_code_200(self):

        product_detail_responses = [self.product_1_detail_response, self.product_2_detail_response]

        for response in product_detail_responses:
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.resolver_match.func, product_detail)
