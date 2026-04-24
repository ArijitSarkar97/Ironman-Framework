import os
import allure
import pytest
from tests.base_test import BaseTest
from pages.homepage_search_functionality import HomepageSearchFunctionality
from utils.data_reader import get_excel_data

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, "test-data", "checkout_test_data.xlsx")

excel_data = get_excel_data(file_path, "searchproduct")
@pytest.mark.arsha
@allure.epic("pytest-automation")
@allure.feature("Aquatics and Reptiles page")
class TestHomepageSearchFunctionality(BaseTest):
    @allure.story("Home page search functionality ")
    @allure.title("home page search for different products")
    @allure.severity(allure.severity_level.NORMAL)

    @pytest.mark.parametrize('data', excel_data)
    def test_home_page_product_search(self, driver, config, data):
        searchproducts = HomepageSearchFunctionality(driver)
        driver.get(config.get('environments', {}).get('orenge_pet', {}).get('base_url', ''))

        with allure.step('Click on the Search tab'):
            searchproducts.click_on_search_tab()

        with allure.step('enter the text in the Search tab'):
            searchproducts.enter_search_text(data)

        with allure.step('Click on the Search button'):
            searchproducts.click_search_button()

