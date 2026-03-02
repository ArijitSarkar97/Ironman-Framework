import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutPage(BasePage):
    contact_email=(By.ID,'email')
    first_name=(By.ID,'TextField0')
    last_name=(By.ID,'TextField1')
    address=(By.ID,'shipping-address1')
    apartment=(By.ID,'TextField2')
    city=(By.ID,'TextField3')
    state=(By.ID,'Select1')
    pin_code=(By.ID,'TextField4') 
    phone=(By.ID,'TextField5')
    text=(By.XPATH,'//h2')
    
    @allure.step("Enter contact email")
    def enter_contact_email(self, contact_email):
        self.enter_text(self.contact_email, contact_email)

    @allure.step("Enter first name")
    def enter_first_name(self, first_name):
        self.enter_text(self.first_name, first_name)

    @allure.step("Enter last name")
    def enter_last_name(self, last_name):
        self.enter_text(self.last_name, last_name)

    @allure.step("Enter address")
    def enter_address(self, address):
        self.enter_text(self.address, address)

    @allure.step("Enter apartment")
    def enter_apartment(self, apartment):
        self.enter_text(self.apartment, apartment)

    @allure.step("Enter city")
    def enter_city(self, city):
        self.enter_text(self.city, city)

    @allure.step("Enter state")
    def enter_state(self, state):
        self.enter_text(self.state, state)

    @allure.step("Enter pin code")
    def enter_pic_code(self, pic_code):
        self.enter_text(self.pin_code, pic_code)

    @allure.step("Enter phone")
    def enter_phone(self, phone):
        self.enter_text(self.phone, phone)

    @allure.step("get text")
    def get_text(self):
        return self.get_text(self.text)
        
        
        