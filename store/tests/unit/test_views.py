# import pytest
from django.test import TestCase, Client
from django.urls import reverse
from store.views import store


class TestStoreView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_store_template_and_url_status_code_200(self):

        products_url = reverse('store')
        response = self.client.get(products_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.func, store)
