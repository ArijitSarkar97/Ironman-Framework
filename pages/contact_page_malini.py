from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactPage(BasePage):
    NAME_FIELD = (By.ID, "contact-form-name")
    EMAIL_FIELD = (By.ID, "contact-form-email")
    PHONE_FIELD = (By.ID, "contact-form-mobile")
    LOCATION_FIELD = (By.ID, "contact-form-location")
    ENQUIRE_ABOUT = (By.XPATH, "//select[@title='Enquire about']")
    MESSAGE_FIELD = (By.ID, "contact-form-message")
    SEND_BTN = (By.XPATH, "//button[contains(text(),'Send message')]")

    def fill_name(self, name):
        self.enter_text(self.NAME_FIELD, name)

    def fill_email(self, email):
        self.enter_text(self.EMAIL_FIELD, email)

    def fill_phone(self, phone):
        self.enter_text(self.PHONE_FIELD, phone)

    def fill_location(self, location):
        self.enter_text(self.LOCATION_FIELD, location)

    def select_enquire_about(self, option_text):
        element = self.find_element(self.ENQUIRE_ABOUT)
        select = Select(element)
        options = [o.text.strip() for o in select.options]
        if option_text in options:
            select.select_by_visible_text(option_text)

    def fill_message(self, message):
        self.enter_text(self.MESSAGE_FIELD, message)

    def submit_form(self):
        self.scroll_to_element(self.SEND_BTN)
        self.wait_until_clickable(self.SEND_BTN, timeout=15)
        self.click(self.SEND_BTN)

