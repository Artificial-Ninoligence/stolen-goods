from django.test import TestCase, Client
from carts.views import cart, checkout


class TestCartsViews(TestCase):

    def setUp(self):

        self.cart_response = Client().get('/cart/')
        self.checkout_response = Client().get('/cart/checkout/')

    def test_cart_template_and_url_status_code_200(self):

        response = self.cart_response

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.func, cart)

    def test_checkout_template_and_url_status_code_200(self):

        response = self.checkout_response
        expected_url = '/accounts/login/?next=%2Fcart%2Fcheckout%2F'

        self.assertEqual(response.resolver_match.func, checkout)
        self.assertRedirects(response, expected_url, status_code=302, target_status_code=200)