import pytest
import allure
import time
from selenium.webdriver.common.by import By
from tests.base_test import BaseTest
from pages.pet_dog_page import PetDogsPage
from pages.pet_birds_page import PetBirdsPage
from pages.pet_home_page import PetHomePage
from pages.pet_productlist import PetProductListPage
from pages.pet_cart_page import PetWishlist
from pages.pet_checkout_page import PetCheckout

@allure.epic("pytest-automation")
@allure.feature("PetBirdsPage")
class TestPetDogPage(BaseTest):

    @allure.story("test_automation_testing_pra_page_fill_all_inputs")
    @allure.title("test_automation_testing_pra_page_fill_all_inputs Execution")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.functional
    def test_search_dog(self,driver,config):
        homepage_pet = PetHomePage(driver)
        dog_pet = PetDogsPage(driver)
        bird_pet=PetBirdsPage(driver)
        productlist_pet = PetProductListPage(driver)
        wishlist_pet= PetWishlist(driver)
        checkout_pet = PetCheckout(driver)

        driver.get(config.get('environments', {}).get('orenge_pet', {}).get('base_url', ''))

        with allure.step("get text"):
            homepage_pet.get_home_a_text()

        with allure.step("mouse hover"):
            dog_pet.click_dogs()

        # with allure.step("click subcategory"):
        #     homepage_pet.click_on_subcategory()

        with allure.step("click on availability "):
            productlist_pet.click_on_availability()
        #
        # with allure.step("click on in-stock"):
        #     productlist_pet.click_on_instock()

        with allure.step("scroll to product"):
            productlist_pet.scroll_to_product()

        with allure.step("click on product name "):
            productlist_pet.click_on_product()

        with allure.step("click on product name "):
            wishlist_pet.scroll_to_cart()
        with allure.step("click on add to cart"):
            wishlist_pet.add_to_cart()

        with allure.step("click on checkout"):
            checkout_pet.click_on_checkout()