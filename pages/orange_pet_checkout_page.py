from pages.base_page import BasePage
from time import sleep
from selenium.webdriver.support.ui import Select
import allure

class OrangePetCheckoutPage(BasePage):
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
    CONTACT = ('xpath','//input[@id="email"]')
    EMAIL_CHECKIN = ('xpath','//input[@id="marketing_opt_in"]')
    FIRSTNAME =('xpath','//input[@placeholder="First name"]')
    LASTNAME =('xpath','//input[@placeholder="Last name"]')
    ADDRESS=('xpath','//input[@placeholder="Address"]')
    APARTMENT=('xpath','//input[@placeholder="Apartment, suite, etc. (optional)"]')
    CITY=('xpath','//input[@placeholder="City"]')
    C_STATE=('xpath','//select[@name="zone"]')
    STATE=('xpath','(//select[@class="ZHJU6 _1k3449n7 _1k3449n5 _1fragemzf oAlPg IWR5K tu1VS"])[2]')
    PINCODE=('xpath','//input[@placeholder="PIN code"]')
    PHONENO=('xpath','//input[@placeholder="Phone"]')
    PAYNOW=('xpath','//button[@id="checkout-pay-button"]')
    SHIPPING_TXT=('xpath','//select[@name="zone"]')






    def __init__(self, driver):
        super().__init__(driver)

    # --- Actions ---

    @allure.step("inputing the contact")
    def entering_contact(self,text):
        self.enter_text(self.CONTACT,text)

    @allure.step("inputing the first name")
    def entering_first_name(self, text):
        self.enter_text(self.FIRSTNAME, text)

    @allure.step("inputing the last name")
    def entering_last_name(self, text):
        self.enter_text(self.LASTNAME, text)

    @allure.step("inputing the address")
    def entering_address(self, text):
        self.enter_text(self.ADDRESS, text)

    @allure.step("inputing the apartment")
    def entering_apartment(self, text):
        self.enter_text(self.APARTMENT, text)

    @allure.step("inputing the city")
    def entering_city(self, text):
        self.enter_text(self.CITY, text)

    @allure.step("scroll to the state")
    def scroll_to_element_shipping(self):
        self.click(self.SHIPPING_TXT)

    @allure.step("click the state")
    def clicking_the_state(self):
        self.click(self.C_STATE)

    @allure.step("inputing the state")
    def select_dropdown_by_text_state(self, text):
        self.select_dropdown_by_text(self.STATE, text)

    @allure.step("inputing the pincode")
    def entering_pincode(self, text):
        self.enter_text(self.PINCODE, text)

    @allure.step("inputing the phone number")
    def entering_phone_no(self, text):
        self.enter_text(self.PHONENO, text)

    @allure.step("clicking the paynow btn")
    def clicking_paynow_btn(self):
        self.click(self.PAYNOW)
        sleep(10)





