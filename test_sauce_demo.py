from selenium import webdriver

from pages.cart_page import CartPage
from pages.checkout_info_page import CheckInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import time
import pytest


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver   
    driver.quit()



def test_saucedemo_workflow(browser):
    browser.get("https://www.saucedemo.com/")

    login_page = LoginPage(browser)
    login_page.enter_username('standard_user')
    login_page.enter_password('secret_sauce')
    login_page.click_login()

    assert 'inventory.html' in browser.current_url  

    inventory_page = InventoryPage(browser)
    inventory_page.add_to_cart()
    inventory_page.go_to_cart()
    time.sleep(5)

    cart_page = CartPage(browser)
    

    cart_page.proceed_to_checkout()

    checkout_info_page = CheckInfoPage(browser)
    checkout_info_page.enter_personal_info("john", "wesley", "12345")

    print(browser.current_url)

    assert 'checkout-step-one.html' in browser.current_url

checkout_info_page.click_continue()

    print(browser.current_url)

    time.sleep(2)

    checkout_overview_page = CheckoutOverviewPage(browser)
    checkout_overview_page.click_finish()

    time.sleep(5)

#     browser.quit()


