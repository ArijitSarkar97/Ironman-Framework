from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class HomePage(BasePage):


    DOGS_LINK = (By.LINK_TEXT, "Dogs")
    CATS_LINK = (By.LINK_TEXT, "Cats")


    def open_dogs_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.DOGS_LINK)
        ).click()

    def open_cats_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CATS_LINK)
        ).click()




