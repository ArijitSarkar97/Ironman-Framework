from time import sleep

import allure

from pages.base_page import BasePage
from selenium.webdriver.common.by import By



class MyCartPage(BasePage):
    Check_out_button=(By.XPATH,"//button[@name='checkout']")

    @allure.step("Click on checkout button")
    def click_on_checkout_button(self):
        self.click(self.Check_out_button)
        