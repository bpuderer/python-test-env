class JohnCleesePage:

    def __init__(self, driver):
        self.driver = driver
        if self.driver.title != "John Cleese - Wikipedia":
            raise ValueError(f"Wrong page. {self.driver.title} instead of John Cleese - Wikipedia")
    
    def take_screenshot(self):
        self.driver.get_screenshot_as_file('screenshots/jmc.png')
