from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
import allure
from selenium.webdriver.support import expected_conditions as EC

class PetHomePage(BasePage):

    CAT = (By.XPATH, "(//a[@class='nav-bar__link link'])[4]")
    DOGS=(By.XPATH, "(//a[@class='nav-bar__link link'])[3]")

    # DRY_FOOD = (By.XPATH, "(//a[text()='Dry Food'])[1]")
    DRY_FOOD=(By.XPATH,'(//a[@class="nav-dropdown__link link"])[1]')
    WET_FOOD=(By.XPATH,'(//a[text()="Wet Food"])[2]')
    # AVAILABILITY = (By.XPATH, "//button[text()='Availability']")
    # IN_STOCK=(By.XPATH, "//label[contains(text(),'In stock')]")
    # PRODUCT_NAME=(By.XPATH, "(//a[@class='product-item__title text--strong link'])[1]")
    # ADD_TO_CART=(By.XPATH,"(//button[text()='Add to cart'])[1]")
    # CHECKOUT=(By.XPATH,'//button[text()="Checkout"]')
    PET_ICON=(By.XPATH,'//img[@class="header__logo-image"]')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Get home_a text")
    def get_home_a_text(self):
        return self.get_text(self.PET_ICON)

    @allure.step("mouse hover cat")
    def click_cat(self):
        return self.click(self.CAT)

    @allure.step("click_on_subcategory")
    def click_on_subcategory(self):
        return self.click(self.DRY_FOOD)

    # @allure.step("click_on_subcategory")
    # def click_on_sub(self):
    #     self.click(self.WET_FOOD)

    # def click_on_availability(self):
    #     self.click(self.AVAILABILITY)

    # def click_on_instock(self):
    #    self.click(self.IN_STOCK)

    # def scroll_to_cart(self):
    #     self.click(self.ADD_TO_CART)
    #
    # def add_to_cart(self):
    #     self.click(self.ADD_TO_CART)
    #
    # def click_on_checkout(self):
    #     self.click(self.CHECKOUT)