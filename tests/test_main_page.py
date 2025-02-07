import time
import pytest
from selenium.webdriver.ie.webdriver import WebDriver

from pages import MainPage


@pytest.mark.smoke
def test_guest_can_to_go_login_page(browser: WebDriver, proxy: None) -> None:
    page = MainPage(browser=browser)
    page.open()
    login_page = page.go_to_login_page()
    assert login_page.title == 'Войти или зарегистрироваться | Oscar - Sandbox'
