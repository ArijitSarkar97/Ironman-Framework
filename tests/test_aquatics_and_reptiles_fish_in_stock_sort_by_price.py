import pytest
import time
import allure
from config.environment import Environment
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from tests.base_test import BaseTest
from pages.aquatics_and_reptiles_fish_in_stock_sort_by_price import AquaticsandReptilesfiler
@pytest.mark.arsha
@allure.epic("pytest-automation")
@allure.feature("Aquatics and Reptiles page")
class TestAquaticsandReptiles(BaseTest):
    @allure.story("Aquatics_and_reptiles_stock_items_filter_condition")
    @allure.title("Aquatics_and_reptiles_stock_items_filter_condition_by_price_low_to_high")
    @allure.severity(allure.severity_level.NORMAL)

    def test_aquatics_and_reptiles_stock_items_filter_condition(self,driver,config):
        aquaticsandreptiles = AquaticsandReptilesfiler(driver)
        driver.get(config.get('environments', {}).get('orenge_pet', {}).get('base_url', ''))

        with allure.step('Navigation to home is sucessfull'):
            aquaticsandreptiles.get_home_a_text()
            assert 'Home' in aquaticsandreptiles.get_home_a_text()

        with allure.step('hover over to aquatics and reptiles'):
            aquaticsandreptiles.hover_over_aquatics_and_reptiles()
            assert 'Fish','Turtle' in aquaticsandreptiles.get_text()

        with allure.step('Click on fish dropdown'):
            aquaticsandreptiles.click_on_fish()

        with allure.step('click on avalibility element'):
            aquaticsandreptiles.click_on_avalibility_element()

        with allure.step('scroll to  element'):
            aquaticsandreptiles.scroll_to_sort_by_feature()

        with allure.step('click on sort by feature'):
            aquaticsandreptiles.click_on_sort_by()

        with allure.step('click on sort by feature price low to high'):
            aquaticsandreptiles.click_on_sort_by_price_low_to_high ()


        with allure.step("Fetch first two product prices"):
            first_price = aquaticsandreptiles.get_first_product_price()
            second_price = aquaticsandreptiles.get_second_product_price()

        with allure.step("Verify products are sorted correctly"):
            assert first_price <= second_price, \
                f"Sorting failed! First: {first_price}, Second: {second_price}"


