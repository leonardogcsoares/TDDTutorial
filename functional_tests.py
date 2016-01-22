import unittest
from selenium import webdriver

class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):
        # Edith has heard about a cool new online to-do app. She goes to the home
        # page to check it out.
        self.browser.get('http://localhost:8000')
        
        # She notices the page title and header mentioned to-do lists
        self.assertIn('To-Do', self.browser.title)
        
# Will only be true if user is running this particular file as a script.
if __name__ == '__main__':
    unittest.main()