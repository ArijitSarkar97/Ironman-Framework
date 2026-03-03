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


@allure.epic("pytest-automation")
@allure.feature("AutomationTestingPraPage")
class TestSmallAnimals(BaseTest):

    @allure.story("test_automation_testing_pra_page_fill_all_inputs")
    @allure.title("test_automation_testing_pra_page_fill_all_inputs Execution")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.functional
    def test_small_animals(self, driver, config):


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
            small_animals.enter_email_ID("pratheshmanickkam.95@gmail.com")
            self.logger.info("Enter Email ID")
        with allure.step("Select Email me and with new offers"):
            small_animals.click_email_me_with_news()
            self.logger.info("Select Email me with news and offers")
        with allure.step("Select by Country"):
            small_animals.select_by_country()
            self.logger.info("Select by Country")
        with allure.step("Enter First Name"):
            small_animals.enter_first_name("Prathesh")
            self.logger.info("Enter First Name")
        with allure.step("Enter Last Name"):
            small_animals.enter_last_name("Manickkam")
            self.logger.info("Enter Last Name")
        with allure.step("Enter address"):
            small_animals.enter_address("Sriranga,Trichy,TamilNadu")
            self.logger.info("Enter Address")
        with allure.step("Enter Apartment"):
            small_animals.enter_apartment("MN Gurugokulam")
            self.logger.info("Enter Apartment")
        with allure.step("Enter City Name"):
            small_animals.enter_city("Tiruchirappalli")
            self.logger.info("Enter City")
        with allure.step("Select State"):
            small_animals.select_state("Karnataka")
            self.logger.info("Select State")
        with allure.step("Enter Phone"):
            small_animals.enter_PINCODE("620006")
            self.logger.info("Enter Phone")
        with allure.step("Orange Pet Nutrition"):
            pelleted_food.scroll_orange_text()
            self.logger.info("Click Orange Pet")
        with allure.step("Click Orange Pet Nutrition"):
            pelleted_food.click_orange_text()
            self.logger.info("Click Orange Pet")
        with allure.step("Hover over small animals"):
            pelleted_food.hover_to_small_animals()
            self.logger.info("Hover over small animals")
        with allure.step("Click Palleted Food"):
            pelleted_food.select_palleted_food()
            self.logger.info("Click Palleted Food")
        with allure.step("Click to filter dropdown"):
            small_animals.click_filter_dropdown()
            self.logger.info("Click filter dropdown")
        with allure.step("Click to checkbox"):
            small_animals.select_checkbox()
            self.logger.info("Click Checkbox")
        with allure.step("Scroll down to Element"):
            pelleted_food.scroll_to_pet_prod()
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
            small_animals.enter_email_ID("pratheshmanickkam.95@gmail.com")
            self.logger.info("Enter Email ID")
        with allure.step("Select Email me and with new offers"):
            small_animals.click_email_me_with_news()
            self.logger.info("Select Email me with news and offers")
        with allure.step("Select by Country"):
            small_animals.select_by_country()
            self.logger.info("Select by Country")
        with allure.step("Enter First Name"):
            small_animals.enter_first_name("Prathesh")
            self.logger.info("Enter First Name")
        with allure.step("Enter Last Name"):
            small_animals.enter_last_name("Manickkam")
            self.logger.info("Enter Last Name")
        with allure.step("Enter address"):
            small_animals.enter_address("Sriranga,Trichy,TamilNadu")
            self.logger.info("Enter Address")
        with allure.step("Enter Apartment"):
            small_animals.enter_apartment("MN Gurugokulam")
            self.logger.info("Enter Apartment")
        with allure.step("Enter City Name"):
            small_animals.enter_city("Tiruchirappalli")
            self.logger.info("Enter City")
        with allure.step("Select State"):
            small_animals.select_state("Karnataka")
            self.logger.info("Select State")
        with allure.step("Enter Phone"):
            small_animals.enter_PINCODE("620006")
            self.logger.info("Enter Phone")
        with allure.step("Orange Pet Nutrition"):
            pelleted_food.scroll_orange_text()
            self.logger.info("Click Orange Pet")
        with allure.step("Click Orange Pet Nutrition"):
            pelleted_food.click_orange_text()
            self.logger.info("Click Orange Pet")
        with allure.step("Hover over small animals"):
            pelleted_food.hover_to_small_animals()
            self.logger.info("Hover over small animals")
        with allure.step("Select Supplement"):
            supplements.click_supplements()
            self.logger.info("Select Supplement")
        with allure.step("Click to filter dropdown"):
            small_animals.click_filter_dropdown()
            self.logger.info("Click filter dropdown")
        with allure.step("Click to checkbox"):
            small_animals.select_checkbox()
            self.logger.info("Click Checkbox")
        with allure.step("Scroll down to Element"):
            supplements.scroll_to_supplements()
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
            small_animals.enter_email_ID("pratheshmanickkam.95@gmail.com")
            self.logger.info("Enter Email ID")
        with allure.step("Select Email me and with new offers"):
            small_animals.click_email_me_with_news()
            self.logger.info("Select Email me with news and offers")
        with allure.step("Select by Country"):
            small_animals.select_by_country()
            self.logger.info("Select by Country")
        with allure.step("Enter First Name"):
            small_animals.enter_first_name("Prathesh")
            self.logger.info("Enter First Name")
        with allure.step("Enter Last Name"):
            small_animals.enter_last_name("Manickkam")
            self.logger.info("Enter Last Name")
        with allure.step("Enter address"):
            small_animals.enter_address("Sriranga,Trichy,TamilNadu")
            self.logger.info("Enter Address")
        with allure.step("Scroll to Shipping Method"):
            small_animals.scroll_to_state()
            self.logger.info("Scroll to Info")
        with allure.step("Enter Apartment"):
            small_animals.enter_apartment("MN Gurugokulam")
            self.logger.info("Enter Apartment")
        with allure.step("Enter City Name"):
            small_animals.enter_city("Tiruchirappalli")
            self.logger.info("Enter City")

        with allure.step("Select State"):
            small_animals.select_state("Karnataka")
            self.logger.info("Select State")

        with allure.step("Enter PinCode"):
            small_animals.enter_PINCODE("620006")
            self.logger.info("Enter PinCode")
        with allure.step("Enter Phone"):
            small_animals.enter_phone("9342765674")
            self.logger.info("Enter Phone")


