from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.monty_pythons_flying_circus_locators import MontyPythonsFlyingCircusLocators
from pages.john_cleese_page import JohnCleesePage


class MontyPythonsFlyingCircusPage():

    PAGE_TITLE = "Monty Python's Flying Circus - Wikipedia"

    def __init__(self, driver):
        self.driver = driver

    def on_mpfc_page(self):
        return self.driver.title == MontyPythonsFlyingCircusPage.PAGE_TITLE

    def click_john_cleese_link(self):
        """Clicks the John Cleese Link

        Returns:
            [JohnCleesePage]: [Instance of JohnCleesePage Page Object]
        """
        wait = WebDriverWait(self.driver, timeout=10)
        wait.until(EC.presence_of_element_located(MontyPythonsFlyingCircusLocators.JOHN_CLEESE_LINK)).click()
        return JohnCleesePage(self.driver)
