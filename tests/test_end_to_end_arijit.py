import pytest
import time
import allure
from config.environment import Environment
from tests.base_test import BaseTest
from pages.home_page_Arijit import OrangePetHomePage
from pages.product_list_page_Arijit import OrangePetProductListPage


@allure.epic("pytest-automation")
@allure.feature("Orange_pet")

class TestOrengePetLogin(BaseTest):

    @allure.story("test_automation_testing_pra_page_fill_all_inputs")
    @allure.title("test_automation_testing_pra_page_fill_all_inputs Execution")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.arijit
    def test_end_to_end(self, driver, config):

        # Initialize Page Objects
        homepage = OrangePetHomePage(driver)
        product_list_page=OrangePetProductListPage(driver)

        driver.get(config.get('environments', {}).get('orenge_pet', {}).get('base_url', ''))
        with allure.step(f"1. Hover to Dog\n"):
            homepage.hover_to_dog()
            self.logger.info("Hover on Dog Module")

        with allure.step(f"2. Click on Dry food \n"):
            homepage.click_on_dog_dryfood()
            self.logger.info("Clicked on Dog dry food successfully")

        with allure.step(f"3. Click on filter \n"):
            product_list_page.click_on_in_stock()
            product_list_page.get_all_product()
            time.sleep(10)
            self.logger.info("Clicked on Dog dry food successfully")

