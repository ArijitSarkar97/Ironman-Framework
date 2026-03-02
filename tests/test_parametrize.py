import pytest
from time import sleep
import allure
from pages.orange_pet_home_page import OrangePetHomePage
from pages.orange_pet_catalogue_page import OrangePetCataloguePage
from pages.orange_pet_product_page import OrangePetProductPage
from pages.orange_pet_cart_page import OrangePetCartPage
from pages.orange_pet_checkout_page import OrangePetCheckoutPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from tests.base_test import BaseTest
from pages.automation_testing_pra_page import AutomationTestingPraPage
from utils.data_reader import read_excel_data


@allure.epic("pytest-automation")
@allure.feature("AutomationTestingPraPage")
class TestOrangePetLogin(BaseTest):
    data=read_excel_data(r"/Users/erajee/PycharmProjects/Ironman-Framework/test data/checkout_test_data.xlsx")

    @allure.story("test_automation_testing_pra_page_fill_all_inputs")
    @allure.title("test_automation_testing_pra_page_fill_all_inputs Execution")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.functional

    @pytest.mark.parametrize("Email,FirstName,LastName,Address,Apartment,City,State,PINCode,Phone",data)
    def test_orange_pet_homepage(self, driver, config,Email,FirstName,LastName,Address,Apartment,City,State,PINCode,Phone):

        catalogue=OrangePetCataloguePage(driver)
        login = OrangePetHomePage(driver)
        product = OrangePetProductPage(driver)
        cart = OrangePetCartPage(driver)
        checkout = OrangePetCheckoutPage(driver)

        driver.get(config.get('environments', {}).get('test', {}).get('base_url', ''))
        with allure.step("click my account not clicked"):
            login.click_account()
            self.logger.info("click my account")

        with allure.step("entering the username"):
            login.entering_account_name("plimpton8@gmail.com")
            self.logger.info("entering the username")

        with allure.step("entering the password"):
            login.entering_account_password("Zaccheo@99")
            self.logger.info("entering the password")
            sleep(5)

        with allure.step("clicking the logo btn"):
            login.click_logo_btn()
            self.logger.info("clicking the logo btn")

        # with allure.step("selecting the categories"):
        #     login.selecting_categories("Animals & Pet Supplies")
        #     self.logger.info("selecting the categories")

        with allure.step("clicking the search bar"):
            login.click_search_bar()
            self.logger.info("clicking the search bar")

        with allure.step("entering the input"):
            login.entering_input("dry food")
            self.logger.info("entering the input")

        with allure.step("clicking the search btn"):
            login.click_search_btn()
            self.logger.info("clicking the search btn")

        with allure.step("clicking availability"):
            catalogue.click_availability_filter()
            self.logger.info("clicking the availability filter")

        with allure.step("clicking instock"):
            catalogue.click_in_stock()
            self.logger.info("clicking instock")

        with allure.step("clicking the product"):
            catalogue.clicking_the_product()
            self.logger.info("clicking the product")

        with allure.step("scroll to add to cart"):
            product.scroll_to_element_add_to_cart()
            self.logger.info("scroll to add to cart")

        with allure.step("Increasing the quantity"):
            product.click_increase_btn()
            self.logger.info("Increasing the quantity")

        with allure.step("clicking the add to cart btn"):
            product.clicking_the_add_to_cart_btn()
            self.logger.info("clicking the add to cart btn")

        with allure.step("clicking the checkout btn"):
            cart.click_checkout_btn()
            self.logger.info("clicking the checkout btn")

        with allure.step("entering the contact"):
            checkout.entering_contact(Email)
            self.logger.info("entering the contact")

        with allure.step("entering the first name"):
            checkout.entering_first_name(FirstName)
            self.logger.info("entering the first name")

        with allure.step("entering the last name"):
            checkout.entering_last_name(LastName)
            self.logger.info("entering the last name")

        with allure.step("entering the address"):
            checkout.entering_address(Address)
            self.logger.info("entering the address")

        with allure.step("entering the apartment"):
            checkout.entering_apartment(Apartment)
            self.logger.info("entering the apartment")

        with allure.step("entering the city"):
            checkout.entering_city(City)
            self.logger.info("entering the city")

        with allure.step("scroll to the state"):
            checkout.scroll_to_element_shipping()
            self.logger.info("scroll to the state")

        with allure.step("clicking the state"):
            checkout.clicking_the_state()
            self.logger.info("clicking the state")

        with allure.step("selecting the state"):
            checkout.select_dropdown_by_text_state(State)
            self.logger.info("selecting the state")

        with allure.step("entering the pincode"):
            checkout.entering_pincode(PINCode)
            self.logger.info("entering the pincode")

        with allure.step("entering the phone number"):
            checkout.entering_phone_no(Phone)
            self.logger.info("entering the phone number")



