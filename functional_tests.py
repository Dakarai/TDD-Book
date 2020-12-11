from selenium import webdriver
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
        self.fail('Finish the test!')

        # user invited to enter a to-do item straight away

        # user types "feed kitties" into a text box

        # when the user presses enter, the page updates, and now the page lists "feed kitties" as an item
        # in the to-do list

        # there is still a text box inviting the user to add another item. they enter "clean litter box"

        # the page updates again, and now shows both items on their list

        # the user wonders if the site will remember their list. then they see that the site has generated
        # a unique url for her (there is also some explanatory text to that efffect)

        # the user visits that url and sees their to-do list is still there

        # the user exits the page

if __name__ == '__main__':
    unittest.main()