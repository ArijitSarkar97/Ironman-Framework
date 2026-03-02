from pages.base_page import BasePage
import allure

class Checkout(BasePage):
    HOME_BUTTON=("xpath",'//h2[text()="Orange Pet Nutrition"]')
    EMAIL_INPUT = ("xpath", "//input[@type='email' or contains(@name, 'email')]")
    FIRST_NAME_INPUT = ("xpath", "//input[contains(@name, 'firstName')]")
    LAST_NAME_INPUT = ("xpath", "//input[contains(@name, 'lastName')]")
    ADDRESS_INPUT = ("xpath", "//input[contains(@name, 'address1')]")
    APARTMENT_INPUT = ("xpath", "//input[contains(@name, 'address2')]")
    CITY_INPUT = ("xpath", "//input[contains(@name, 'city')]")
    STATE_INPUT = ("xpath", "//select[contains(@name, 'zone')]")
    PINCODE_INPUT = ("xpath", "//input[contains(@name, 'postalCode')]")
    PHONE_INPUT = ("xpath", "//input[@type='tel' or contains(@name, 'phone')]")
    CONTINUE_BUTTON = ("xpath", "//button[contains(., 'Continue')]")

    def click_home_button(self):
        self.hover_over_element(self.HOME_BUTTON)
        self.click(self.HOME_BUTTON)
        
    def enter_email(self, email):
        self.enter_text(self.EMAIL_INPUT, email)

    def enter_first_name(self, first_name):
        self.enter_text(self.FIRST_NAME_INPUT, first_name)

    def enter_last_name(self, last_name):
        self.enter_text(self.LAST_NAME_INPUT, last_name)

    def enter_address(self, address):
        self.enter_text(self.ADDRESS_INPUT, address)

    def enter_apartment(self, apartment):
        self.enter_text(self.APARTMENT_INPUT, apartment)

    def enter_city(self, city):
        self.enter_text(self.CITY_INPUT, city)

    def enter_state(self, state):
        self.enter_text(self.STATE_INPUT, state)

    def enter_pincode(self, pincode):
        self.enter_text(self.PINCODE_INPUT, pincode)

    def enter_phone(self, phone):
        self.enter_text(self.PHONE_INPUT, phone)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)