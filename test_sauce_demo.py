import unittest
from selenium import webdriver

from pages.cart_page import CartPage
from pages.checkout_info_page import CheckInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import time


class TestSauceDemo(unittest.TestCase):
    def test_saucedemo_workflow(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        login_page = LoginPage(driver)
        login_page.enter_username('standard_user')
        login_page.enter_password('secret_sauce')
        login_page.click_login()

        self.assertIn('inventory.html', driver.current_url) # Verifying the successfull login

        # Interact with inventory page
        inventory_page = InventoryPage(driver)
        inventory_page.add_to_cart()
        inventory_page.go_to_cart()
        time.sleep(5)

        cart_page = CartPage(driver)
        # time.sleep(5)

        cart_page.proceed_to_checkout()

        checkout_info_page = CheckInfoPage(driver)
        checkout_info_page.enter_personal_info("john", "wesley", "12345")

        print(driver.current_url)

        self.assertIn('checkout-step-one.html', driver.current_url)

        checkout_info_page.click_continue()

        print(driver.current_url)

        time.sleep(2)

        checkout_overview_page = CheckoutOverviewPage(driver)
        checkout_overview_page.click_finish()

        time.sleep(5)

        driver.quit()


if __name__ == "__main__":
    unittest.main()


