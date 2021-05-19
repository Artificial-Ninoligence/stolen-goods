from django.test import TestCase, LiveServerTestCase, Client
# from django.urls import reverse
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from time import sleep
from accounts.views import register, login
# import pytest


class TestRegisterView(TestCase):

    def setUp(self):

        self.client = Client()

    def test_register_template_and_url_status_code_200(self):

        response = self.client.get('/accounts/register/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.func, register)


class TestLoginView(LiveServerTestCase):

    def setUp(self):

        self.cm_driver = webdriver.Chrome()
        self.client = Client()

    def test_login_form(self):

        cm_driver = self.cm_driver

        cm_driver.get('http://127.0.0.1:8000/accounts/login/')
        cm_driver.find_element_by_id('login-email').send_keys('nino.lindenberg@code.berlin')
        cm_driver.find_element_by_id('login-password').send_keys('password123!')
        cm_driver.find_element_by_id('login-submit').click()
        sleep(3)

        assert 'You are now logged in.' in cm_driver.page_source

    def test_admin_login_form(self):

        cm_driver = self.cm_driver

        cm_driver.get('http://127.0.0.1:8000/stolen-goods-admin/')
        cm_driver.find_element_by_id('id_username').send_keys('admin@sg.wtf')
        cm_driver.find_element_by_id('id_password').send_keys('admin')
        cm_driver.find_element_by_css_selector('input[type=submit]').click()
        sleep(3)

        assert 'Django administration' in cm_driver.page_source

    def test_login_template_and_url_status_code_200(self):

        response = self.client.get('/accounts/login/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.resolver_match.func, login)

    def tearDown(self):
        self.cm_driver.quit()
