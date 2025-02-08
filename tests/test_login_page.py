import time
from selenium.webdriver.ie.webdriver import WebDriver

from pages import LoginPage


def test_login_with_invalid_data(browser: WebDriver, proxy: None) -> None:
    page = LoginPage(browser)
    page.open()
    page.login_email_field.send_keys('someemail@mail.ru')
    page.login_password_field.send_keys('somepassword')
    page.sign_in_button.click()
    assert len(page.invalid_email_or_password_error_blocks) == 2
