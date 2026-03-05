# import pytest
# import allure
# from tests.base_test import BaseTest
# from pages.treats_page import TreatsPage
# from utils.data_reader_prathesh import read_excel_data
#
# @allure.epic("pytest-automation")
# @allure.feature("Treats Navigation")
# class TestTreatsPage(BaseTest):
#
#     # @allure.story("test_navigate_to_small_animal_treats")
#     # @allure.title("Navigate to Small Animal Treats Page")
#     # @allure.severity(allure.severity_level.NORMAL)
#
#     file_path=r"test-data\checkout_test_data.xlsx"
#     sheet_name="CheckoutData"
#     test_data=read_excel_data(file_path)
#
#     @pytest.mark.parametrize("email,firstname,lastname,address,apartment,city,state_name,pincode,phone",test_data)
#     def test_small_animal_treats_navigation(self, driver, config,email,firstname,lastname,address,apartment,city,state_name,pincode,phone):
#         driver.get(config.get('environments', {}).get('test', {}).get('base_url', ''))
#         treats_page = TreatsPage(driver)
#
#         with allure.step("Hover on Small Animals menu"):
#             treats_page.hover_small_animals()
#
#         with allure.step("Click Treats under Small Animals"):
#             treats_page.click_treats()
#
#         with allure.step("Hover on Small Animals menu"):
#             treats_page.hover_small_animals()
#
#         with allure.step("Click Treats under Small Animals"):
#             treats_page.click_bedding()
#
#         with allure.step("Click Treats under Small Animals"):
#             treats_page.click_availability()
#
#         with allure.step("click on checkbox"):
#             treats_page.click_instock()
#
#         with allure.step("click on the product"):
#             treats_page.click_item()
#
#
#
#         with allure.step("click on add to cart button"):
#             treats_page.click_cart()
#
#         with allure.step("click on checkout button"):
#             treats_page.click_checkout()
#
#         with allure.step("Enter Email"):
#             treats_page.enter_email(email)
#
#         with allure.step("Enter First Name"):
#             treats_page.enter_firstname(firstname)
#
#         with allure.step("Enter Last Name"):
#             treats_page.enter_lastname(lastname)
#
#         with allure.step("Enter Address"):
#             treats_page.enter_address(address)
#
#
#         with allure.step("Enter Apartment"):
#             treats_page.enter_apartment(apartment)
#
#
#         with allure.step("Enter City"):
#             treats_page.enter_city(city)
#
#         with allure.step("Enter City"):
#             treats_page.select_state(state_name)
#
#
#         with allure.step("Enter Pincode"):
#             treats_page.enter_pincode(pincode)
#
#         with allure.step("Enter Phone Number"):
#             treats_page.enter_phone(phone)
#
