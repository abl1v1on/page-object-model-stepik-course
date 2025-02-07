from selenium.webdriver.ie.webdriver import WebDriver

from pages import BasePage


class MainPage(BasePage):
    def __init__(self, browser: WebDriver) -> None:
        super().__init__(browser)
        self.url = self.url
