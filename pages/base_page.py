from dataclasses import dataclass
from typing import TYPE_CHECKING
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver

if TYPE_CHECKING:
    from pages import LoginPage


@dataclass(frozen=True)
class BasePageLocator:
    login_link: tuple[str, str] = (By.ID, 'login_link')


class BasePage:
    def __init__(self, browser: WebDriver, timeout: int = 10) -> None:
        self.browser = browser
        self.browser.implicitly_wait(timeout)
        self.url = 'http://selenium1py.pythonanywhere.com/ru'
    
    def open(self) -> None:
        self.browser.get(self.url)

    def find(self, by: str, value: str) -> WebElement:
        return self.browser.find_element(by, value)

    def is_element_present(self, by: str, value: str):
        try:
            self.find(by, value)
        except NoSuchElementException:
            return False
        return True

    def go_to_login_page(self) -> 'LoginPage':
        from pages import LoginPage

        self.login_link.click()
        return LoginPage(self.browser)

    @property
    def title(self) -> str:
        return self.browser.title

    @property
    def login_link(self) -> WebElement:
        return self.find(*BasePageLocator.login_link)
