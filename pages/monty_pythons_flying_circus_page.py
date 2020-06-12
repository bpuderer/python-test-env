from selenium.webdriver.support import expected_conditions as EC

from locators.monty_pythons_flying_circus_locators import MontyPythonsFlyingCircusLocators
from pages.base_page import BasePage
from pages.john_cleese_page import JohnCleesePage


class MontyPythonsFlyingCircusPage(BasePage):

    PAGE_TITLE = "Monty Python's Flying Circus - Wikipedia"

    def on_correct_page(self):
        return self.get_title() == MontyPythonsFlyingCircusPage.PAGE_TITLE

    def click_john_cleese_link(self):
        """Clicks the John Cleese Link

        Returns:
            [JohnCleesePage]: [Instance of JohnCleesePage Page Object]
        """
        self.wait.until(EC.presence_of_element_located(MontyPythonsFlyingCircusLocators.JOHN_CLEESE_LINK)).click()
        #self.driver.find_element(*MontyPythonsFlyingCircusLocators.JOHN_CLEESE_LINK).click()
        return JohnCleesePage(self.driver)
