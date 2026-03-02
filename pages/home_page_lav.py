import allure

from pages.base_page import BasePage
from selenium.webdriver.common.by import By



class HomePage(BasePage):
    My_account_link=(By.PARTIAL_LINK_TEXT,'My account')
    Email_textfield=(By.ID,'login-customer[email]')
    Password_textfield=(By.ID,'login-customer[password]')
    Login_button=(By.XPATH,'//button[normalize-space()="Login"]')
    Aquatics_and_Reptiles=(By.PARTIAL_LINK_TEXT,'Aquatics & Reptiles')
    Fish=(By.XPATH,'(//ul[@id="desktop-menu-0-7"]//a)[1]')
    Turtle=(By.XPATH,'(//ul[@id="desktop-menu-0-7"]//a)[2]')
    Tortoise=(By.XPATH,'(//ul[@id="desktop-menu-0-7"]//a)[3]')
    
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click My_account_Link")
    def click_My_account_Link(self):
        self.click(self.My_account_link)

    @allure.step("Enter email ID")
    def enter_email_id(self,email):
        self.enter_text(self.Email_textfield,email)
        
    @allure.step("Enter Password")
    def enter_password(self,password):
        self.enter_text(self.Password_textfield,password)

    @allure.step("Click My_account_Link")
    def click_on_login_button(self):
        self.click(self.Login_button)

    @allure.step("Mouse hover on Aquatics_and_Reptiles")
    def mouse_hover_on_Aquatics_and_Reptiles(self):
        self.hover_over_element(self.Aquatics_and_Reptiles)

    @allure.step("Click on fish link")
    def click_on_fish_link(self):
        self.click(self.Fish)

    @allure.step("Click Turtle")
    def click_on_Turtle_link(self):
        self.click(self.Turtle)

    @allure.step("Click Tortoise")
    def click_on_Tortoise_link(self):
        self.click(self.Tortoise)
    
    
    
        
    
    
    
    

    
    
    
    
    