from pages.base_page import BasePage
import allure

class DogPoopBags(BasePage):
    PRODUCT = ("xpath","//a[.='Earth Rated Pet Grooming Wipes - 100 Count']")
    ADD_TO_CART = ("xpath","//button[.='Add to cart']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("select product")
    def select_product(self):
        return self.click(self.PRODUCT)

    @allure.step("add product to cart")
    def add_to_cart(self):
        return self.click(self.ADD_TO_CART)


