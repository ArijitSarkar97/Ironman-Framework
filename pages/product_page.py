import allure

from pages.base_page import BasePage
from selenium.webdriver.common.by import By



class ProductPage(BasePage):
    Add_to_cart_button=(By.XPATH,"//button[normalize-space()='Add to cart']")

    @allure.step("scroll to add to cart button")
    def scroll_on_add_to_cart_button(self):
        self.scroll_to_element(self.Add_to_cart_button)

    @allure.step("Click on add to cart button")
    def click_on_add_to_cart_button(self):
        self.click(self.Add_to_cart_button)