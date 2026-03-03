from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    EMAIL_FIELD = (By.ID, "email")

    def is_checkout_loaded(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.EMAIL_FIELD)
            )
            return True
        except:
            return False