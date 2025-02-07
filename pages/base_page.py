from typing import TYPE_CHECKING
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver

if TYPE_CHECKING:
    from pages import LoginPage


class BasePage:
    def __init__(self, browser: WebDriver) -> None:
        self.browser = browser
        self.url = 'http://selenium1py.pythonanywhere.com/ru'
    
    def open(self) -> None:
        self.browser.get(self.url)

    def find(self, by: str, value: str) -> WebElement:
        return self.browser.find_element(by, value)

    def go_to_login_page(self) -> 'LoginPage':
        from pages import LoginPage

        self.login_link.click()
        return LoginPage(self.browser)

    @property
    def title(self) -> str:
        return self.browser.title

    @property
    def login_link(self) -> WebElement:
        return self.find(By.ID, 'login_link')
