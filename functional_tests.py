from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit

    def test_can_start_a_list_and_retrieve_it_later(self):

        # User goes to the homepage
        self.browser.get('http://localhost:8000')

        # user reads the page title
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # user invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # user types "feed kitties" into a text box
        inputbox.send_keys('Feed kitties')

        # when the user presses enter, the page updates, and now the page lists "feed kitties" as an item
        # in the to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Feed kitties' for row in rows))

        # there is still a text box inviting the user to add another item. they enter "clean litter box"
        self.fail('Finish the test!')

        # the page updates again, and now shows both items on their list

        # the user wonders if the site will remember their list. then they see that the site has generated
        # a unique url for her (there is also some explanatory text to that efffect)

        # the user visits that url and sees their to-do list is still there

        # the user exits the page


if __name__ == '__main__':
    unittest.main()