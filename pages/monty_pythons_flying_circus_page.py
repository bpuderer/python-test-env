from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.monty_pythons_flying_circus_locators import MontyPythonsFlyingCircusLocators
from pages.john_cleese_page import JohnCleesePage


class MontyPythonsFlyingCircusPage:

    PAGE_TITLE = "Monty Python's Flying Circus - Wikipedia"

    def __init__(self, driver):
        self.driver = driver
        if self.driver.title != MontyPythonsFlyingCircusPage.PAGE_TITLE:
            raise ValueError(f"Wrong page. {self.driver.title} instead of {MontyPythonsFlyingCircusPage.PAGE_TITLE}")

        self.wait = WebDriverWait(self.driver, timeout=10)

    def click_john_cleese_link(self):
        """Clicks the John Cleese Link

        Returns:
            [JohnCleesePage]: [Instance of JohnCleesePage Page Object]
        """
        self.wait.until(EC.presence_of_element_located(MontyPythonsFlyingCircusLocators.JOHN_CLEESE_LINK)).click()
        #self.driver.find_element(*MontyPythonsFlyingCircusLocators.JOHN_CLEESE_LINK).click()
        return JohnCleesePage(self.driver)
