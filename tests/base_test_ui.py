import os

from selenium import webdriver

from framework.config import settings
from pages.monty_pythons_flying_circus_page import MontyPythonsFlyingCircusPage
from tests.base_test import BaseTestCase


class BaseUiTestCase(BaseTestCase):

    def setUp(self):
        if settings['browser'].lower() == 'firefox':
            self.driver = webdriver.Firefox()
        elif settings['browser'].lower() == 'chrome':
            self.driver = webdriver.Chrome()
        elif settings['browser'].lower() == 'headless chrome':
            opts = webdriver.ChromeOptions()
            opts.add_argument('headless')
            self.driver = webdriver.Chrome(options=opts)
        else:
            raise Exception(f'Browser {settings["browser"]} is not supported')

        self.driver.get('https://en.wikipedia.org/wiki/Monty_Python%27s_Flying_Circus')
        self.home_page = MontyPythonsFlyingCircusPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def take_screenshot(self, filename):
        self.driver.get_screenshot_as_file(os.path.join('screenshots', filename))
