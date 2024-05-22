from tests.base_test_ui import BaseUiTestCase


class SeleniumExample(BaseUiTestCase):

    def test_selenium_example(self):
        #self.assertTrue(self.home_page.on_mpfc_page)
        cleese_page = self.home_page.click_john_cleese_link()
        self.take_screenshot('jmc.png')
        self.assertTrue(cleese_page.on_cleese_page())
        self.assertEqual(cleese_page.get_num_marriages(), 4)
