from django.test import TestCase, Client
from accounts.views import register, login, logout
# import pytest


class TestRegisterView(TestCase):

    def setUp(self):

        self.response = Client().get('/accounts/register/')

    def test_register_template_and_url_status_code_200(self):

        response = self.response

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.func, register)


class TestLoginView(TestCase):

    def setUp(self):

        self.response = Client().get('/accounts/login/')

    def test_login_template_and_url_status_code_200(self):

        response = self.response

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.func, login)
        

class TestLogoutView(TestCase):

    def setUp(self):

        self.response = Client().get('/accounts/logout/')
        self.expected_url = '/accounts/login/?next=%2Faccounts%2Flogout%2F'

    def test_logout_redirect_and_url_status_code_200(self):

        response = self.response
        expected_url = self.expected_url

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.resolver_match.func, logout)
        self.assertRedirects(response, expected_url, status_code=302, target_status_code=200)
