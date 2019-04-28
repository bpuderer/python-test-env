from locators.monty_pythons_flying_circus_locators import MontyPythonsFlyingCircusLocators


class MontyPythonsFlyingCircusPage:

    def __init__(self, driver):
        self.driver = driver
        if self.driver.title != "Monty Python's Flying Circus - Wikipedia":
            raise ValueError(f"Wrong page. {self.driver.title} instead of Monty Python's Flying Circus - Wikipedia")

    def click_john_cleese_link(self):
        """click the John Cleese link"""
        element = self.driver.find_element(*MontyPythonsFlyingCircusLocators.JOHN_CLEESE_LINK)
        element.click()
