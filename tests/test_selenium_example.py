from pages.john_cleese_page import JohnCleesePage
from pages.monty_pythons_flying_circus_page import MontyPythonsFlyingCircusPage
from tests.base_test_ui import BaseUiTestCase


class SeleniumExample(BaseUiTestCase):

    def test_selenium_example(self):
        monty_python = MontyPythonsFlyingCircusPage(self.driver)
        john_cleese = monty_python.click_john_cleese_link()
        john_cleese.take_screenshot('jmc.png')
        self.assertEqual(john_cleese.get_title(), JohnCleesePage.PAGE_TITLE)
