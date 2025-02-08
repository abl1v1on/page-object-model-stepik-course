import os
import pytest
from typing import Generator
from selenium.webdriver import Chrome
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='session')
def proxy() -> Generator:
    os.system('proxy -d')
    yield
    os.system('proxy -e')


@pytest.fixture(scope='session')
def options() -> Options:
    options = Options()
    # options.add_argument('--headless')
    return options


@pytest.fixture(scope='session')
def service() -> Service:
    return Service(
        executable_path=ChromeDriverManager().install()
    )


@pytest.fixture(scope='function')
def browser(
        options: Options, 
        service: Service
    ) -> Generator[WebDriver, None, None]:
    browser = Chrome(options=options, service=service)
    yield browser
    browser.quit()
