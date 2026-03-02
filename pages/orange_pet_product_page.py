from pages.base_page import BasePage
from time import sleep
from selenium.webdriver.support.ui import Select
import allure

class OrangePetProductPage(BasePage):
    # --- Locators (format: "locator_type", "locator_value") ---
    LOGO=('xpath','//img[@src="//www.orangepet.in/cdn/shop/files/orange_pet_140x@2x.png?v=1649050236"]')
    ACCOUNT= ('xpath','//a[contains(text(),"My account ")]')
    ACCOUNT_NAME = ('id','login-customer[email]')
    ACCOUNT_PASSWORD= ('id','login-customer[password]')
    SEARCH_BAR = ('xpath','//div/input[@class="search-bar__input"]')
    SEARCH_BUTTON = ('xpath','//button[@class="search-bar__submit"]')
    CATEGORIES = ('css selector','select#search-product-type')
    AVAILABILITY= ('xpath','//div/button[text()="Availability"]')
    INSTOCK=('xpath','//input[@id="filter.v.availability-1"]')
    PRODUCT=('xpath','(//div[@class="product-item product-item--vertical  1/3--tablet-and-up 1/4--desk"])[1]')
    ADDTOCART=('xpath','//button[text()="Add to cart"]')
    QUANTITYINC = ('xpath','(//button[@class="quantity-selector__button"])[2]')





    def __init__(self, driver):
        super().__init__(driver)

    # --- Actions ---

    @allure.step("scroll to add to cart")
    def scroll_to_element_add_to_cart(self):
        self.scroll_to_element(self.ADDTOCART)

    @allure.step("click quantity increase btn")
    def click_increase_btn(self):
        self.click(self.QUANTITYINC)

    @allure.step("click add to cart btn")
    def clicking_the_add_to_cart_btn(self):
        self.click(self.ADDTOCART)
        sleep(5)
