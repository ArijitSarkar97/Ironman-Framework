
import pytest

import allure

from pages.checkout1_page import CheckoutPage
from pages.fish_page import FishPage
from pages.home_page_lav import HomePage
from pages.my_cart_page import MyCartPage
from pages.product_page import ProductPage
from pages.turtle_page import TurtlePage
from tests.base_test import BaseTest

class TestLogin(BaseTest):
    def test_browser_launch(self,driver,config):
        driver.get(config.get('environments', {}).get('aqua', {}).get('base_url', ''))
        homepage=HomePage(driver)
        fish=FishPage(driver)
        product=ProductPage(driver)
        turtle=TurtlePage(driver)
        cart=MyCartPage(driver)
        checkout1=CheckoutPage(driver)
        
        with allure.step(f"1.Hover on Aquatics_and_Reptiles  \n"):
            homepage.mouse_hover_on_Aquatics_and_Reptiles()
            self.logger.info("Hover on Aquatics_and_Reptiles executed successfully")
        with allure.step(f"1.click on fish  \n"):
            homepage.click_on_fish_link()
            self.logger.info("click on fish executed successfully")
        with allure.step(f"1.click on availability  \n"):
            fish.click_on_availability_link()
            self.logger.info("click on availability executed successfully")
        with allure.step(f"1.click on in stock checkbox  \n"):
            fish.click_on_in_stock()
            self.logger.info("click on in stock executed successfully")
        with allure.step(f"1.click on product \n"):
            fish.click_on_product_link()
            self.logger.info("click on product executed successfully")
        with allure.step(f"1.click on add to cart \n"):
            product.scroll_on_add_to_cart_button()
            self.logger.info("click on add to cart executed successfully")
                             
        with allure.step(f"1.click on add to cart \n"):
            product.click_on_add_to_cart_button()
            self.logger.info("click on add to cart executed successfully")
            
        '''to add product from turtle'''  
        with allure.step(f"1.Hover on Aquatics_and_Reptiles  \n"):
            homepage.mouse_hover_on_Aquatics_and_Reptiles()
            self.logger.info("Hover on Aquatics_and_Reptiles executed successfully")
            
        with allure.step(f"1.click on Turtle  \n"):
            homepage.click_on_Turtle_link()
            self.logger.info("click on Turtle executed successfully")

        with allure.step(f"1.click on availability  \n"):
            turtle.click_on_availability_link()
            self.logger.info("click on availability executed successfully")
        with allure.step(f"1.click on in stock checkbox  \n"):
            turtle.click_on_in_stock()
            self.logger.info("click on in stock executed successfully")
        with allure.step(f"1.click on product \n"):
            turtle.click_on_product_link()
            self.logger.info("click on product executed successfully")
        with allure.step(f"1.click on add to cart \n"):
            product.scroll_on_add_to_cart_button()
            self.logger.info("click on add to cart executed successfully")

        with allure.step(f"1.click on add to cart \n"):
            product.click_on_add_to_cart_button()
            self.logger.info("click on add to cart executed successfully")
            
        with allure.step("6. Proceed to checkout"):
            cart.click_on_checkout_button()
            self.logger.info("click on add to CHECKOUT executed successfully")
            
        # with allure.step("7. Enter checkout details"):
        #     assert checkout1.get_text=="Orange Pet Nutrition"
        #     self.logger.info("get text executed successfully")
            
            
        '''to add product from tortoise'''   
        # with allure.step(f"1.click on Tortoise  \n"):
        #     homepage.click_on_Tortoise_link()
        #     self.logger.info("click on Tortoise executed successfully")
        
        '''no product in tortoise'''
        
    
            
            