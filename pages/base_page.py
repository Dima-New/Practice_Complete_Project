from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver, url):
        self.driver: WebDriver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)
