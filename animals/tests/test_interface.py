import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class FunctionalTest(StaticLiveServerTestCase):
    fixtures = ['animals.json', 'users.json',]

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(1)

    def tearDown(self):
        self.browser.quit()

    def test_pet_tracker_interface(self):
        self.browser.get(self.live_server_url)

        self.browser.find_element_by_id('id_username').send_keys('admin')
        self.browser.find_element_by_id('id_password').send_keys('password')
        self.browser.find_element_by_id('submit').click()
        time.sleep(.5)

        page_title = "Pet Tracker"
        self.assertEqual(self.browser.title, page_title)
        header_h1 = self.browser.find_element_by_tag_name('h1')
        self.assertEqual(header_h1.text, page_title)

        # list all pets

        # list all dogs

        # list all cats

        # view one dog

        # view one cat

        # add a dog

        # add a cat

        # delete a dog

        # delete a cat
