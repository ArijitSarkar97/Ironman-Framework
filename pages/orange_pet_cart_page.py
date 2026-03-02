from pages.base_page import BasePage
from time import sleep
from selenium.webdriver.support.ui import Select
import allure

class OrangePetCartPage(BasePage):
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
    CHECKOUT_BUTTON=('xpath','//button[text()="Checkout"]')





    def __init__(self, driver):
        super().__init__(driver)

    # --- Actions ---

    @allure.step("clicking checkout button")
    def click_checkout_btn(self):
        self.click(self.CHECKOUT_BUTTON)
        sleep(5)


