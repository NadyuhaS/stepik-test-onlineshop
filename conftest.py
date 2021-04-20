from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default="ru", help="my option: type1 or type2"
    )

@pytest.fixture
def browser( request ):
    user_lang = request.config.getoption( "--language" )

    chrome_opt = Options()
    chrome_opt.add_experimental_option("prefs", {"intl.accept_languages": user_lang } )

    browser = webdriver.Chrome( options = chrome_opt )
    yield browser
    browser.quit()
