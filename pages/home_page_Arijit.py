from pages.base_page import BasePage
import allure

class OrangePetHomePage(BasePage):
    HOME_PAGE_LOGO=("css","header__logo-link")
    MY_ACCOUNT=("xpath","//a[contains(text(),'My account')]")
    EMAIL=("id","login-customer[email]")
    PASSWORD = ("id", "login-customer[password]")
    LOGIN_BUTTON=("xpath","//button[contains(text(),'Login')]")
    DOG_MODULE=("xpath","(//a[contains(text(),'Dogs')])[2]")
    DOG_DRY_FOOD=("xpath","(//a[@href='/collections/dry-dog-food'])[2]")
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click on My Account.")
    def click_on_my_account(self):
        self.click(self.MY_ACCOUNT)

    @allure.step("Login to Account with valid email and password")
    def login(self,email,password):
        self.enter_text(self.EMAIL,email)
        self.enter_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    @allure.step("Hover to dog")
    def hover_to_dog(self):
        self.hover_over_element(self.DOG_MODULE)

    @allure.step("Hover to dog")
    def click_on_dog_dryfood(self):
        self.click(self.DOG_DRY_FOOD)

