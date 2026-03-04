from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class PetWishlist(BasePage):
    ADD_TO_CART = (By.XPATH,"(//button[text()='Add to cart'])[1]")

    def scroll_to_cart(self):
        self.scroll_to_element(self.ADD_TO_CART)

    def add_to_cart(self):
        self.click(self.ADD_TO_CART)