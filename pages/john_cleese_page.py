from selenium.webdriver.common.by import By

class JohnCleesePage():

    PAGE_TITLE = "John Cleese - Wikipedia"

    def __init__(self, driver):
        self.driver = driver

    def on_cleese_page(self):
        return self.driver.title == JohnCleesePage.PAGE_TITLE

    def get_num_marriages(self):
        marriages = self.driver.find_elements(By.CSS_SELECTOR, '.infobox-data .marriage-display-ws')
        return len(marriages)
