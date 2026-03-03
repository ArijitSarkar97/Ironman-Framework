
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    ADD_BUTTONS =  [
        (By.XPATH, "//button[contains(text(),'Add')]"),
        (By.CSS_SELECTOR, "button[name='add']")
    ]

    def add_to_cart(self):
        for locator in self.ADD_BUTTONS:
            if self.is_element_visible(locator, timeout=5):
                self.scroll_to_element(locator)
                self.click(locator)
                print("Add to cart clicked")
                return
        raise Exception("Add to Cart button not found on this product page")