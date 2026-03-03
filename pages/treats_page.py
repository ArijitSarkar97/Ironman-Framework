from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TreatsPage(BasePage):

    SMALL_ANIMALS = (By.XPATH, "(//a[contains(text(),'Small')])[2]")

    TREATS = (By.XPATH, "(//a[text()='Treats'])[4]")
    BEDDING=(By.XPATH,"(//a[text()='Bedding and Hay'])[2]")
    AVAILABILITY=(By.XPATH,"//button[text()='Availability']")
    INSTOCK=(By.XPATH,'//input[@id="filter.v.availability-1"]')
    ITEM=(By.CSS_SELECTOR,'img[data-media-id*="26482510856374"][srcset*="//www.o"]')
    ADDTOCART=(By.XPATH,'(//button[text()="Add to cart"])[1]')
    CHECKOUT=(By.XPATH,'//button[text()="Checkout"]')
    CHECKOUT_BUTTON = (By.XPATH, "//button[text()='Checkout']")
    EMAIL = (By.XPATH, '//input[@id="email"]')
    FIRSTNAME = (By.NAME, 'firstName')
    LASTNAME = (By.NAME, "lastName")
    APARTMENT = (By.XPATH, '//input[@placeholder="Apartment, suite, etc. (optional)"]')
    CITY = (By.NAME, "address2")
    state_dropdown=(By.XPATH, '//select[@name="zone"]')


    ADDRESS = (By.NAME, "address1")

    PINCODE = (By.NAME, "postalCode")
    PHONE = (By.NAME, "phone")


    def hover_small_animals(self):
        self.hover_over_element(self.SMALL_ANIMALS)

    def click_treats(self):
        self.click(self.TREATS)

    def hover_small_animals(self):
        self.hover_over_element(self.SMALL_ANIMALS)

    def click_bedding(self):
        self.click(self.BEDDING)

    def click_availability(self):
        self.click(self.AVAILABILITY)

    def click_instock(self):
        self.click(self.INSTOCK)

    def click_item(self):
        self.click(self.ITEM)



    def click_cart(self):
        self.click(self.ADDTOCART)

    def click_checkout(self):
        self.click(self.CHECKOUT)

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def enter_email(self, email):
        self.enter_text(self.EMAIL, email)

    def enter_firstname(self, firstname):
        self.enter_text(self.FIRSTNAME, firstname)

    def enter_lastname(self, lastname):
        self.enter_text(self.LASTNAME, lastname)

    def enter_address(self, address):
        self.enter_text(self.ADDRESS, address)

    def enter_apartment(self, apartment):
        self.enter_text(self.APARTMENT, apartment)

    def enter_city(self, city):
        self.enter_text(self.CITY, city)

    def select_state(self, state_name):
        self.select_dropdown_by_text(self.state_dropdown, state_name)

    def enter_pincode(self, pincode):
        self.enter_text(self.PINCODE, pincode)

    def enter_phone(self, phone):
        self.enter_text(self.PHONE, phone)
