from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_basket( browser ) :
    browser.get( link )

    button = WebDriverWait( browser, 20 ).until(
        lambda browser : browser.find_element_by_css_selector( 'button.btn-add-to-basket' )
    )

    assert button != None, f"No add to basket button in {link}"

def test_work_button( browser ):
    browser.get(link)

    button = WebDriverWait(browser, 20).until(
        lambda browser: browser.find_element_by_css_selector('button.btn-add-to-basket')
    )
    button.click()

    message_success = WebDriverWait(browser, 20).until(
        lambda browser: browser.find_element_by_css_selector('.alert-success .alertinner strong')
    )

    assert message_success != None, f"Button doesn't work corecktly in {link}"
