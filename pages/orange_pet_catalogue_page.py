from pages.base_page import BasePage
from time import sleep
from selenium.webdriver.support.ui import Select
import allure

class OrangePetCataloguePage(BasePage):
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




    def __init__(self, driver):
        super().__init__(driver)

    # --- Actions ---

    @allure.step("click availability filter")
    def click_availability_filter(self):
        self.click(self.AVAILABILITY)

    @allure.step("click Instock")
    def click_in_stock(self):
        self.click(self.AVAILABILITY)

    @allure.step("click the product")
    def clicking_the_product(self):
        self.click(self.PRODUCT)
        sleep(5)
