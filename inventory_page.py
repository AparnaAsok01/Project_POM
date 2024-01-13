from selenium.webdriver.common.by import By
from .base_page import BasePage

class InventoryPage(BasePage):

    ADD_TO_CART_BUTTONS = (By.XPATH, "//button[text()='Add to cart']")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def add_to_cart(self):
        add_buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        if add_buttons:
            add_buttons[0].click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART_ICON).click()

