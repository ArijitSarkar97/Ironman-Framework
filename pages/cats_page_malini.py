

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CatsPage(BasePage):

    FIRST_PRODUCT = (By.XPATH, "(//a[contains(@href,'/products/')])[1]")

    def open_first_product(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FIRST_PRODUCT)
        ).click()