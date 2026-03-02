from pages.base_page import BasePage
import allure

class ProductDetailsPage(BasePage):
    ADD_TO_CART=("xpath",'//button[text()="Add to cart"]')

    def click_add_to_cart(self):
        self.hover_over_element(self.ADD_TO_CART)
        self.click(self.ADD_TO_CART)

    # def check_if_product_present(self):
    #     if