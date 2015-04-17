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

    def get_text_for_items(self, item_selector):
        return [item.text for item in
                self.browser.find_elements_by_css_selector(item_selector)]

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
        self.assertEqual(self.get_text_for_items('#pet-list td'), [
            '1',
            'Fido',
            'Dog',
            'Labrador Retriever',
            'May 11, 2013',
            '2',
            'Felix',
            'Cat',
            'Bombay',
            'Nov 1, 2011'
        ])


        # list all dogs
        toggle_cats = self.browser.find_element_by_id('toggle-showing-cats')
        toggle_cats.click()
        self.assertEqual(self.get_text_for_items('#pet-list td'), [
            '1',
            'Fido',
            'Dog',
            'Labrador Retriever',
            'May 11, 2013'
        ])
        toggle_cats.click()

        # list all cats
        toggle_dogs = self.browser.find_element_by_id('toggle-showing-dogs')
        toggle_dogs.click()
        self.assertEqual(self.get_text_for_items('#pet-list td'), [
            '2',
            'Felix',
            'Cat',
            'Bombay',
            'Nov 1, 2011'
        ])
        toggle_dogs.click()

        # view one dog
        pet1 = self.browser.find_element_by_id('pet-1')
        pet1.click()
        time.sleep(.5)

        self.assertEqual(
            self.browser.find_element_by_tag_name('h2').text, "Fido")
        self.assertEqual(self.get_text_for_items('.pet-details td'), [
            '1',
            'Dog canis lupus familiaris',
            'Labrador Retriever',
            'May 11, 2013',
            'Delete'
        ])
        self.browser.find_element_by_class_name('close-pet-details').click()

        # view one cat
        pet2 = self.browser.find_element_by_id('pet-2')
        pet2.click()
        time.sleep(.5)

        self.assertEqual(
            self.browser.find_element_by_tag_name('h2').text, "Felix")
        self.assertEqual(self.get_text_for_items('.pet-details td'), [
            '2',
            'Cat felis catus',
            'Bombay',
            'Nov 1, 2011',
            'Delete'
        ])
        self.browser.find_element_by_class_name('close-pet-details').click()

        # add a dog

        # add a cat

        # delete a dog

        # delete a cat
