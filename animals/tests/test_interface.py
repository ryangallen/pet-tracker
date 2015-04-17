import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert

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
        time.sleep(.25)

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

        add_pet = self.browser.find_element_by_id('add-pet')

        # add a dog
        add_pet.click()
        self.browser.find_element_by_id('add-dog').click()
        self.browser.find_element_by_id('add-siberian-husky').click()
        self.browser.find_element_by_id('add-name').send_keys('Balto')
        self.browser.find_element_by_id('add-birthday').send_keys('1919-09-02')
        self.browser.find_element_by_id('save-new-pet').click()
        time.sleep(.25)
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
            'Nov 1, 2011',
            '3',
            'Balto',
            'Dog',
            'Siberian Husky',
            'Sep 2, 1919'
        ])

        # add a cat
        add_pet.click()
        self.browser.find_element_by_id('add-cat').click()
        self.browser.find_element_by_id('add-bombay').click()
        self.browser.find_element_by_id('add-name').send_keys('Salem')
        self.browser.find_element_by_id('add-birthday').send_keys('1924-10-31')
        self.browser.find_element_by_id('save-new-pet').click()
        time.sleep(.25)
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
            'Nov 1, 2011',
            '3',
            'Balto',
            'Dog',
            'Siberian Husky',
            'Sep 2, 1919',
            '4',
            'Salem',
            'Cat',
            'Bombay',
            'Oct 31, 1924',
        ])

        # delete a dog
        self.browser.find_element_by_id('pet-1').click()

        verify_delete = self.browser.find_element_by_id('verify-delete')
        delete_pet = self.browser.find_element_by_id('delete-pet')

        verify_delete.click()
        self.browser.find_element_by_css_selector(
            '#delete-verification input').send_keys("Fido")
        delete_pet.click()
        Alert(self.browser).accept()
        time.sleep(3)

        self.assertEqual(self.get_text_for_items('#pet-list td'), [
            '2',
            'Felix',
            'Cat',
            'Bombay',
            'Nov 1, 2011',
            '3',
            'Balto',
            'Dog',
            'Siberian Husky',
            'Sep 2, 1919',
            '4',
            'Salem',
            'Cat',
            'Bombay',
            'Oct 31, 1924',
        ])

        # delete a cat
        self.browser.find_element_by_id('pet-2').click()
        verify_delete.click()
        self.browser.find_element_by_css_selector(
            '#delete-verification input').send_keys("Felix")
        delete_pet.click()
        Alert(self.browser).accept()
        time.sleep(.25)

        self.assertEqual(self.get_text_for_items('#pet-list td'), [
            '3',
            'Balto',
            'Dog',
            'Siberian Husky',
            'Sep 2, 1919',
            '4',
            'Salem',
            'Cat',
            'Bombay',
            'Oct 31, 1924',
        ])
