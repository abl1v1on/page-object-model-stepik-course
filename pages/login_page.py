from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages import BasePage


class LoginPage(BasePage):
    def __init__(self, browser: WebDriver) -> None:
        super().__init__(browser)
        self.url = 'accounts/login/'
    
    @property
    def login_email_field(self) -> WebElement:
        return self.find(By.NAME, 'login-username')

    @property
    def login_password_field(self) -> WebElement:
        return self.find(By.NAME, 'login-password')
    
    @property
    def forget_password_link(self) -> WebElement:
        return self.find(By.XPATH, '//a[text()="Я забыл пароль"]')

    @property
    def sign_in_button(self) -> WebElement:
        return self.find(By.NAME, 'login_submit')
