from selenium import webdriver

from framework.testbase import BaseTestCase
from pages.monty_pythons_flying_circus_page import MontyPythonsFlyingCircusPage
from pages.john_cleese_page import JohnCleesePage


class SeleniumExample(BaseTestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://en.wikipedia.org/wiki/Monty_Python%27s_Flying_Circus')

    def tearDown(self):
        self.driver.close()

    def test_selenium_example(self):
        driver = self.driver
        monty_python = MontyPythonsFlyingCircusPage(driver)
        monty_python.click_john_cleese_link()

        john_cleese = JohnCleesePage(driver)
        john_cleese.take_screenshot()
