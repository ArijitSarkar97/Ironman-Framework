
import allure

from pages.base_page import BasePage
from selenium.webdriver.common.by import By



class TurtlePage(BasePage):
    Availability_link=(By.XPATH,"//button[contains(text(),'Availability')]")
    In_stock_checkbox=(By.XPATH,'//input[@id="filter.v.availability-1"]')
    Product_link=(By.XPATH,'//img[@data-media-id="29158580486326"]')

    @allure.step("Click on availability link")
    def click_on_availability_link(self):
        self.click(self.Availability_link)

    @allure.step("Click on in stock checkbox")
    def click_on_in_stock(self):
        self.click(self.In_stock_checkbox)

    @allure.step("Click on product link")
    def click_on_product_link(self):
        self.click(self.Product_link)