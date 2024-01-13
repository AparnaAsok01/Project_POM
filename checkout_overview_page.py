from selenium.webdriver.common.by import By
from .base_page import BasePage


class CheckoutOverviewPage(BasePage):
    FINISH_BUTTON = (By.XPATH, "// button[@class ='btn btn_action btn_medium cart_button']")

    def click_finish(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()
