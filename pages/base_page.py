import os.path

from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

        def __init__(self, driver):
            self.driver = driver
            self.wait = WebDriverWait(self.driver, timeout=10)

        def get_title(self):
            return self.driver.title

        def take_screenshot(self, filename):
            self.driver.get_screenshot_as_file(os.path.join('screenshots', filename))
