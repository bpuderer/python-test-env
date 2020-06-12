from pages.base_page import BasePage


class JohnCleesePage(BasePage):

    PAGE_TITLE = "John Cleese - Wikipedia"

    def on_correct_page(self):
        return self.get_title() == JohnCleesePage.PAGE_TITLE
