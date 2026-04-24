
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CartPage(BasePage):

    CART_ICON = (By.XPATH, "//a[contains(@href,'/cart')]")
    CHECKOUT_BTN = (By.NAME, "checkout")

    def open_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CART_ICON)
        ).click()

    def click_checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_BTN)
        ).click()