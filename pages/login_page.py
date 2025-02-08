from dataclasses import dataclass
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages import BasePage


@dataclass(frozen=True)
class LoginPageLocator:
    login_email: tuple[str, str] = (By.NAME, 'login-username')
    login_password: tuple[str, str] = (By.NAME, 'login-password')
    forget_password: tuple[str, str] = (By.XPATH, '//a[text()="Я забыл пароль"]')
    sign_in: tuple[str, str] = (By.NAME, 'login_submit')
    error_blocks: tuple[str, str] = (By.CSS_SELECTOR, '.alert.alert-danger')


class LoginPage(BasePage):
    def __init__(self, browser: WebDriver) -> None:
        super().__init__(browser)
        self.url = self.url + '/accounts/login/'

    @property
    def login_email_field(self) -> WebElement:
        return self.find(*LoginPageLocator.login_email)

    @property
    def login_password_field(self) -> WebElement:
        return self.find(*LoginPageLocator.login_password)

    @property
    def forget_password_link(self) -> WebElement:
        return self.find(*LoginPageLocator.forget_password)

    @property
    def sign_in_button(self) -> WebElement:
        return self.find(*LoginPageLocator.sign_in)
    
    @property
    def invalid_email_or_password_error_blocks(self) -> list[WebElement]:
        return self.browser.find_elements(*LoginPageLocator.error_blocks)
