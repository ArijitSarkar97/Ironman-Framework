from time import sleep

import pytest

import allure

from pages.home_page_lav import HomePage
from tests.base_test import BaseTest
class TestLogin(BaseTest):
    def test_browser_launch(self,driver,config):
        driver.get(config.get('environments', {}).get('aqua', {}).get('base_url', ''))
        homepage=HomePage(driver)
        
        with allure.step(f"1. Click submit_button button \n"):
            homepage.click_My_account_Link()
            self.logger.info("Click My account link executed successfully")
        with allure.step(f"2. Click enter email textfield \n"):
            homepage.enter_email_id('rangamlavanyars@gmail.com')
            self.logger.info("Click enter email executed successfully")
        with allure.step(f"3. Click enter password textfeild \n"):
            homepage.enter_password('Srinivas@jaya1')
            self.logger.info("Click enter password textfeild executed successfully")
        with allure.step(f"1. Click logout button \n"):
            homepage.click_on_login_button()
            self.logger.info("Click login button executed successfully")
            
            
        
        
    