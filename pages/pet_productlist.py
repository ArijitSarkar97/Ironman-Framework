from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class PetProductListPage(BasePage):

    AVAILABILITY = (By.XPATH, "//button[text()='Availability']")
    IN_STOCK = (By.XPATH, "//label[contains(text(),'In stock')]")
    PRODUCT_NAME = (By.XPATH, "(//a[@class='product-item__title text--strong link'])[1]")

    def click_on_availability(self):
        self.click(self.AVAILABILITY)

    def click_on_instock(self):
        self.click(self.IN_STOCK)

    def scroll_to_product(self):
        self.scroll_to_element(self.PRODUCT_NAME)

    def click_on_product(self):
        self.click(self.PRODUCT_NAME)