class JohnCleesePage:

    PAGE_TITLE = "John Cleese - Wikipedia"

    def __init__(self, driver):
        self.driver = driver

        if self.driver.title != JohnCleesePage.PAGE_TITLE:
            raise ValueError(f"Wrong page. {self.driver.title} instead of {JohnCleesePage.PAGE_TITLE}")

    def get_title(self):
        return self.driver.title

    def take_screenshot(self):
        self.driver.get_screenshot_as_file('screenshots/jmc.png')
