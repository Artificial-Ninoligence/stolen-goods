from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pytest


@pytest.mark.skip(reason="No CI setup for selenium in Github Actions")
class TestAccountForms(LiveServerTestCase):

    def setUp(self):

        self.cm_driver = webdriver.Chrome('drivers/chromedriver')
        self.cm_driver.maximize_window()

    def test_user_login_form(self):

        cm_driver = self.cm_driver

        cm_driver.get('http://127.0.0.1:8000/accounts/login/')
        cm_driver.find_element_by_id('login-email').send_keys('nino.lindenberg@code.berlin')
        cm_driver.find_element_by_id('login-password').send_keys('password123!')
        cm_driver.find_element_by_id('login-submit').click()
        sleep(3)

        assert 'Dashboard' in cm_driver.title
        assert 'You are now logged in.' in cm_driver.page_source

    def test_adminuser_login_form(self):

        cm_driver = self.cm_driver

        cm_driver.get('http://127.0.0.1:8000/stolen-goods-admin/')
        cm_driver.find_element_by_id('id_username').send_keys('admin@sg.wtf')
        cm_driver.find_element_by_id('id_password').send_keys('admin')
        cm_driver.find_element_by_css_selector('input[type=submit]').click()
        sleep(3)

        assert 'Django site admin' in cm_driver.title
        assert 'Django administration' in cm_driver.page_source

    def test_edit_user_profile_form(self):

        cm_driver = self.cm_driver

        cm_driver.get('http://127.0.0.1:8000/accounts/edit_profile')
        cm_driver.find_element_by_id('login-email').send_keys('nino.lindenberg@code.berlin')
        cm_driver.find_element_by_id('login-password').send_keys('password123!')
        cm_driver.find_element_by_id('login-submit').click()

        for element in cm_driver.find_elements_by_class_name('form-control'):
            element.clear()

        cm_driver.find_element_by_id('id_first_name').send_keys('Nino')
        cm_driver.find_element_by_id('id_last_name').send_keys('Lindenberg')
        cm_driver.find_element_by_id('dob').send_keys('04.01.1990')
        cm_driver.find_element_by_id('id_address_line_1').send_keys('Storkower Str. 108')
        cm_driver.find_element_by_id('id_address_line_2').send_keys('17/07')
        cm_driver.find_element_by_id('id_postal_code').send_keys('10407')
        cm_driver.find_element_by_id('id_city').send_keys('Berlin')
        cm_driver.find_element_by_id('id_state').send_keys('Berlin')
        cm_driver.find_element_by_id('id_country').send_keys('Germany')
        cm_driver.find_element_by_id('edit_profile-save').send_keys(Keys.RETURN)
        sleep(3)

        assert 'Your profile has been updated' in cm_driver.page_source
        # assert 'Django' in cm_driver.page_source

    def tearDown(self):
        self.cm_driver.quit()
