import os
import pytest
import allure
import time
from utils.data_reader_varshitha import read_excel_data
from pages.HomePage_varshitha import Test_HomePage
from tests.base_test import BaseTest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, "test-data", "checkout_test_data.xlsx")

excel_data = read_excel_data(file_path, "CheckoutData")


@allure.epic("pytest-automation")
@allure.feature("catmodule")
class Test_cat_mod(BaseTest):

    @allure.story("validating the products")
    @allure.title("testing")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.functional
    
    @pytest.mark.parametrize("data", excel_data)
    def test_catmod(self, driver, config, data):

        TestHomePage = Test_HomePage(driver)

        driver.get(config['environments']['catmod']['base_url'])

        with allure.step("Clicking on cat"):
            TestHomePage.click_on_cat()

        with allure.step("Clicking on litter"):
            TestHomePage.clickingonlitter()

        with allure.step("Clicking on availability"):
            TestHomePage.clicking_on_availability()

        with allure.step("Clicking on instock"):
            TestHomePage.clicking_on_instock_option()

        time.sleep(5)

        with allure.step("Validating number of items"):
            TestHomePage.check_the_number_of_items()

        with allure.step("Clicking product"):
            TestHomePage.clickontheproduct()

        with allure.step("Adding to cart"):
            TestHomePage.addtocart()

        with allure.step("Checkout"):
            TestHomePage.checkingout()

        # ✅ Excel data used correctly
        with allure.step("Filling checkout details"):
            TestHomePage.fill_checkout_details(
                data["Email"],
                data["FirstName"],
                data["LastName"],
                data["Apartment"],
                data["City"]
            )

