from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class PetCheckout(BasePage):

    CHECKOUT = (By.XPATH,'//button[text()="Checkout"]')
    EMAIL=(By.ID,'email')
    # FNAME=(By.ID."TextField0")

    def click_on_checkout(self):
        self.click(self.CHECKOUT)

    def add_email(self):
        self.enter_text(self.EMAIL)

    # def add_name(self):
    #     self.enter_text(self.FNAME)