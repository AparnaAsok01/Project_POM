from selenium.webdriver.common.by import By
from .base_page import BasePage


class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.XPATH, "//button[@class='btn btn_action btn_medium checkout_button ']")

    def proceed_to_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
