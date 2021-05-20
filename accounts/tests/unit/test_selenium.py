from django.test import LiveServerTestCase
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from time import sleep
import pytest


@pytest.mark.skip(reason="No CI setup for selenium in Github Actions")
class TestLoginForm(LiveServerTestCase):

    def setUp(self):

        self.cm_driver = webdriver.Chrome('drivers/chromedriver')

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

    def tearDown(self):
        self.cm_driver.quit()
