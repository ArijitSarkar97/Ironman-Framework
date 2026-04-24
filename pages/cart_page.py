from pages.base_page import BasePage
import allure

class CartPage(BasePage):
    CHECKOUT_BUTTON=('xpath','//button[text()="Checkout"]')
    HOME_BUTTON=('xpath','//a[@class="header__logo-link"]')

    def click_checkout(self):
        self.hover_over_element(self.CHECKOUT_BUTTON)
        self.click(self.CHECKOUT_BUTTON)

    def click_home_button(self):
        self.hover_over_element(self.HOME_BUTTON)
        self.click(self.HOME_BUTTON)