from pages.base_page import BasePage
from config.environment import Environment
import allure

class HomePage(BasePage,Environment):
    MY_ACCOUNT=("xpath",'//a[contains(text(),"My account")]')
    CREATE_YOUR_ACCOUNT=("xpath",'//a[contains(text(),"Create your account")]')
    EMAIL=("id",'login-customer[email]')
    PASSWORD=("id","login-customer[password]")
    SUBMIT_BUTTON=("xpath",'//button[text()="Login"]')
    current_env=Environment("orange")
    BIRDS_DROPDOWN = ("xpath", '//li[@class="nav-bar__item"]/a[text()="Birds"]')
    SEED_BASED_FOOD = ("xpath", '//a[text()="Birds"]/following-sibling::ul/li/a[text()="Seed Based Food"]')
    PELLETED_FOOD = ("xpath", '//a[text()="Birds"]/following-sibling::ul/li/a[text()="Pelleted Food"]')
    SUPPLEMENTS = ("xpath", '//a[text()="Birds"]/following-sibling::ul/li/a[text()="Supplements"]')
    TREATS = ("xpath", '//a[text()="Birds"]/following-sibling::ul/li/a[text()="Treats"]')
    AVAILABILITY_DROPDOWN = ("xpath", '//button[text()="Availability"]')
    IN_STOCK_RADIO = ("xpath", '//input[@id="filter.v.availability-1"]')
    PRODUCTS=("xpath",'(//div[@class="product-list product-list--collection product-list--with-sidebar"]/div)[3]')

    def __init__(self, driver):
        super().__init__(driver)
        self.env = Environment("orange")

    def birds_dropdown(self):
        self.click(self.BIRDS_DROPDOWN)

    @allure.step("clicking on create account button")
    def create_account_button(self):
        self.click(self.MY_ACCOUNT)
        self.click(self.CREATE_YOUR_ACCOUNT)

    def login_account(self):
        self.click(self.MY_ACCOUNT)
        self.enter_text(self.EMAIL,self.env.get_username())
        self.enter_text(self.PASSWORD,self.env.get_password())
        self.click(self.SUBMIT_BUTTON)

    def seed_based_listing_page(self):
        self.hover_over_element(self.BIRDS_DROPDOWN)
        self.click(self.SEED_BASED_FOOD)
        self.click(self.AVAILABILITY_DROPDOWN)
        self.click(self.IN_STOCK_RADIO)

    def pelled_listing_page(self):
        self.hover_over_element(self.BIRDS_DROPDOWN)
        self.click(self.PELLETED_FOOD)
        self.click(self.AVAILABILITY_DROPDOWN)
        self.click(self.IN_STOCK_RADIO)

    def supplement_listing_page(self):
        self.hover_over_element(self.BIRDS_DROPDOWN)
        self.click(self.SUPPLEMENTS)
        self.click(self.AVAILABILITY_DROPDOWN)
        self.click(self.IN_STOCK_RADIO)

    def treat_listing_page(self):
        self.hover_over_element(self.BIRDS_DROPDOWN)
        self.click(self.TREATS)
        self.click(self.AVAILABILITY_DROPDOWN)
        self.click(self.IN_STOCK_RADIO)

    def click_product(self):
        self.hover_over_element(self.PRODUCTS)
        self.click(self.PRODUCTS)



