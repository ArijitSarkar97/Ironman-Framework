import pytest
from time import sleep
import allure
from utils.data_reader import read_test_data

from config.environment import Environment
from pages.home_page_suraj import HomePage
from pages.sign_up_page import SignUpPage
from tests.base_test import BaseTest
from pages.product_details_page import ProductDetailsPage
from pages.cart_page import CartPage
from pages.checkout_page import Checkout

test_data = read_test_data(
    file_path=r"d:\PyCharmMiscProject\Tek_project\orange\Ironman-Framework\checkout_test_data.xlsx", 
    format='excel'
)

class TestBirdsModule(BaseTest):
    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    def test_signup_page(self,driver,config):
        homepage=HomePage(driver)
        signup_page=SignUpPage(driver)
        product_details_page=ProductDetailsPage(driver)
        cart_page=CartPage(driver)
        checkout_page=Checkout(driver)

        driver.get(config.get('environments', {}).get('orange', {}).get('base_url', ''))
        # homepage.create_account_button()
        # signup_page.account_creation()
        # homepage.login_account()
        # sleep(30)

        with allure.step("adding product based on birds seed based foods"):
            homepage.seed_based_listing_page()
            homepage.click_product()
            product_details_page.click_add_to_cart()
            cart_page.click_home_button()
            homepage.pelled_listing_page()
            homepage.click_product()
            product_details_page.click_add_to_cart()
            cart_page.click_home_button()
            homepage.supplement_listing_page()
            homepage.click_product()
            product_details_page.click_add_to_cart()
            cart_page.click_home_button()
            homepage.treat_listing_page()
            homepage.click_product()
            product_details_page.click_add_to_cart()
            cart_page.click_checkout()
            checkout_page.click_home_button()
            sleep(5)
    @pytest.mark.suraj
    @pytest.mark.flaky(reruns=2, reruns_delay=1)
    @pytest.mark.parametrize(
        "email, first_name, last_name, address, apartment, city, state, pincode, phone", 
        test_data
    )
    def test_checkout_form(self, driver,config, email, first_name, last_name, address, apartment, city, state, pincode, phone):
        checkout_page = Checkout(driver)
        homepage = HomePage(driver)
        signup_page = SignUpPage(driver)
        product_details_page = ProductDetailsPage(driver)
        cart_page = CartPage(driver)
        checkout_page = Checkout(driver)

        driver.get(config.get('environments', {}).get('orange', {}).get('base_url', ''))
        with allure.step("adding product based on birds seed based foods"):
            homepage.seed_based_listing_page()
            homepage.click_product()
            product_details_page.click_add_to_cart()
            # cart_page.click_home_button()
            # homepage.pelled_listing_page()
            # homepage.click_product()
            # product_details_page.click_add_to_cart()
            # cart_page.click_home_button()
            # homepage.supplement_listing_page()
            # homepage.click_product()
            # product_details_page.click_add_to_cart()
            # cart_page.click_home_button()
            # homepage.treat_listing_page()
            # homepage.click_product()
            # product_details_page.click_add_to_cart()
            cart_page.click_checkout()
        
        with allure.step(f"Filling checkout form for {first_name} {last_name}"):
            checkout_page.enter_email(email)
            checkout_page.enter_first_name(first_name)
            checkout_page.enter_last_name(last_name)
            checkout_page.enter_address(address)
            checkout_page.enter_apartment(apartment)
            checkout_page.enter_city(city)
            checkout_page.enter_state(state)
            checkout_page.enter_pincode(pincode)
            checkout_page.enter_phone(phone)
            # checkout_page.click_continue()



















