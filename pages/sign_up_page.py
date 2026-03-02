from pages.base_page import BasePage
import allure

class SignUpPage(BasePage):
    FIRST_NAME=("id",'customer[first_name]')
    LAST_NAME=("id",'customer[last_name]')
    EMAIL_ADDRESS=("id","customer[email]")
    PASSWORD=("id","customer[password]")
    CREATE_MY_ACCOUNT_BUTTON=('xpath','//button[text()="Create my account"]')

    @allure.step("creating an account for user")
    def account_creation(self):
        self.enter_text(self.CREATE_MY_ACCOUNT_BUTTON,"Raghav")
        self.enter_text(self.LAST_NAME,"Chaddha")
        self.enter_text(self.EMAIL_ADDRESS,"jrsuraj1998@gmail.com")
        self.enter_text(self.PASSWORD,"123456")
        self.click(self.CREATE_MY_ACCOUNT_BUTTON)

