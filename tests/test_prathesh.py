import pytest
import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from tests.base_test import BaseTest
from pages.SA_Seed_Based_Food import SeedBasedFood
from pages.SA_Pelleted_Food import PelletedFood
from pages.SA_Supplements import Supplements
from utils.data_reader_prathesh import read_excel_data


@allure.epic("pytest-automation")
@allure.feature("AutomationTestingPraPage")
@pytest.mark.flaky(reruns = 2, reruns_delay = 2)
class TestSmallAnimals(BaseTest):
    data = read_excel_data(r"test-data\checkout_test_data.xlsx")

    @allure.story("test_automation_testing_pra_page_fill_all_inputs")
    @allure.title("test_automation_testing_pra_page_fill_all_inputs Execution")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.functional
    @pytest.mark.parametrize("Email,FirstName,LastName,Address,Apartment,City,State,PINCode,Phone",data)
    def test_small_animals(self,driver, config, Email,FirstName,LastName,Address,Apartment,City,State,PINCode,Phone):


        small_animals = SeedBasedFood(driver)
        pelleted_food = PelletedFood(driver)
        supplements = Supplements(driver)
        driver.get(config.get('environments', {}).get('test', {}).get('base_url', ''))

        with allure.step("Hover to Seed based food"):
            small_animals.click_small_animals()
            self.logger.info("Click Seed based food")
        with allure.step("Click to filter dropdown"):
            small_animals.click_filter_dropdown()
            self.logger.info("Click filter dropdown")
        with allure.step("Click to checkbox"):
            small_animals.select_checkbox()
            self.logger.info("Click Checkbox")
        with allure.step("Scroll down to Element"):
            small_animals.scroll_to_pet_prod()
            self.logger.info("Scroll down to Element")
        with allure.step("Click Product Image"):
            small_animals.click_product_image()
            self.logger.info("Click Product Image")
        with allure.step("Scroll to Add to Cart Button"):
            small_animals.scroll_to_add_to_cart()
            self.logger.info("Scroll Add to Cart Button")
        with allure.step("Click Add to Cart Button"):
            small_animals.click_to_add_to_cart()
            self.logger.info("Click Add to Cart Button")
        with allure.step("Scroll to Checkout"):
            small_animals.scroll_to_checkout()
            self.logger.info("Scroll to Checkout")
        with allure.step("Click Checkout Button"):
            small_animals.click_checkout_button()
            self.logger.info("Click Checkout Button")
        with allure.step("Enter Email ID"):
            small_animals.enter_email_ID(Email)
            self.logger.info("Enter Email ID")
        with allure.step("Select Email me and with new offers"):
            small_animals.click_email_me_with_news()
            self.logger.info("Select Email me with news and offers")
        with allure.step("Select by Country"):
            small_animals.select_by_country()
            self.logger.info("Select by Country")
        with allure.step("Enter First Name"):
            small_animals.enter_first_name(FirstName)
            self.logger.info("Enter First Name")
        with allure.step("Enter Last Name"):
            small_animals.enter_last_name(LastName)
            self.logger.info("Enter Last Name")
        with allure.step("Enter address"):
            small_animals.enter_address(Address)
            self.logger.info("Enter Address")
        with allure.step("Enter Apartment"):
            small_animals.enter_apartment(Apartment)
            self.logger.info("Enter Apartment")
        with allure.step("Enter City Name"):
            small_animals.enter_city(City)
            self.logger.info("Enter City")
        with allure.step("Select State"):
            small_animals.select_state(State)
            self.logger.info("Select State")
        with allure.step("Enter Phone"):
            small_animals.enter_PINCODE(PINCode)
            self.logger.info("Enter Phone")
        with allure.step("Enter Phone"):
            small_animals.enter_phone(Phone)
            self.logger.info("Enter Phone")


