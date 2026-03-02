from pages.base_page import BasePage
from time import sleep
from selenium.webdriver.support.ui import Select
import allure

class OrangePetHomePage(BasePage):
    # --- Locators (format: "locator_type", "locator_value") ---
    LOGO=('xpath','//img[@src="//www.orangepet.in/cdn/shop/files/orange_pet_140x@2x.png?v=1649050236"]')
    ACCOUNT= ('xpath','//a[contains(text(),"My account ")]')
    ACCOUNT_NAME = ('id','login-customer[email]')
    ACCOUNT_PASSWORD= ('id','login-customer[password]')
    SEARCH_BAR = ('xpath','//div/input[@class="search-bar__input"]')
    SEARCH_BUTTON = ('xpath','//button[@class="search-bar__submit"]')
    CATEGORIES = ('css selector','select#search-product-type')

    def __init__(self, driver):
        super().__init__(driver)

    # --- Actions ---

    @allure.step("click account")
    def click_account(self):
        self.click(self.ACCOUNT)

    @allure.step("enter the account name")
    def entering_account_name(self, text):
        self.enter_text(self.ACCOUNT_NAME, text)

    @allure.step("enter the account password")
    def entering_account_password(self, text):
        self.enter_text(self.ACCOUNT_PASSWORD, text)

    @allure.step("click search bar")
    def click_search_bar(self):
        self.click(self.SEARCH_BAR)

    @allure.step("enter the input in search bar")
    def entering_input(self,text):
        self.enter_text(self.SEARCH_BAR,text)

    @allure.step("click search button")
    def click_search_btn(self):
        self.click(self.SEARCH_BUTTON)
        sleep(10)

    @allure.step("click logo btn")
    def click_logo_btn(self):
        self.click(self.LOGO)

    @allure.step("click the categories")
    def click_categories(self):
        self.click(self.CATEGORIES)
        sleep(5)

    @allure.step("selecting the categories")
    def selecting_categories(self,text):
        self.select_dropdown_by_text(self.CATEGORIES,text)



