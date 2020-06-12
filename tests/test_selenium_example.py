from selenium import webdriver

from framework.config import settings
from framework.testbase import BaseTestCase
from pages.monty_pythons_flying_circus_page import MontyPythonsFlyingCircusPage
from pages.john_cleese_page import JohnCleesePage


class SeleniumExample(BaseTestCase):

    def setUp(self):
        if settings['browser'].lower() == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()
        self.driver.get('https://en.wikipedia.org/wiki/Monty_Python%27s_Flying_Circus')

    def tearDown(self):
        self.driver.quit()

    def test_selenium_example(self):
        monty_python = MontyPythonsFlyingCircusPage(self.driver)
        john_cleese = monty_python.click_john_cleese_link()
        john_cleese.take_screenshot()
        self.assertEqual(john_cleese.get_title(), "John Cleese - Wikipedia")
