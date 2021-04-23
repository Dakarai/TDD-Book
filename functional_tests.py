from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Check out the app webpage
        self.browser.get("http://localhost:8000")

        # Check the page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test!")

        # Invited to enter a to-do item straight away

        # Types "Buy peacock feathers" into a text box

        # Hit enter, page updates, now the page lists "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box to add another item. Type "Use feathers to make a fly"

        # The page updates again and now shows both items on the list

        # Website generated unique URL with some explanatory text to remember the list

        # Visit the URL and see the list is still there

        # End

if __name__ == '__main__':
    unittest.main()