import pytest
import time
import allure
from config.environment import Environment
from tests.base_test import BaseTest
from pages.home_page_Arijit import OrangePetHomePage


@allure.epic("pytest-automation")
@allure.feature("AutomationTestingPraPage")

class TestOrengePetLogin(BaseTest):

    @allure.story("test_automation_testing_pra_page_fill_all_inputs")
    @allure.title("test_automation_testing_pra_page_fill_all_inputs Execution")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.arijit
    def test_login(self, driver, config):

        # Initialize Page Objects
        homepage = OrangePetHomePage(driver)
        env = Environment("orenge_pet")
        email = env.get_username()
        password = env.get_password()

        driver.get(config.get('environments', {}).get('orenge_pet', {}).get('base_url', ''))
        with allure.step(f"1. Click on My Account \n"):
            homepage.click_on_my_account()

            self.logger.info("Clicked on My Account successfully")
        with allure.step(f"2. Fill email_input with valid data \n"):
            homepage.login(email, password)
            time.sleep(10)
            self.logger.info("Fill email_input with valid data executed successfully")

