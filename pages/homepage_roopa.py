from pages.base_page import BasePage
import allure

class HomePage(BasePage):
    MY_ACCOUNT_LINK = ("xpath","(//a[@href='/account/login'])[2]")
    DOGS_LINK = ("xpath","(//a[contains(.,'Dogs')])[2]")
    VETRINARY_LINK = ("xpath","(//a[.='Veterinary Food'])[2]")
    DENTAL_BONES_LINK = ("xpath","(//a[.='Dental Bones'])[2]")
    POOPBAGS_LINK = ("xpath","(//a[.='Dog Poop Bags'])[2]")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click My account")
    def on_click_myaccount(self):
        return self.click(self.MY_ACCOUNT_LINK)

    @allure.step("Mouse hover on Dogs link")
    def mouse_hover_dogs(self):
        return self.hover_over_element(self.DOGS_LINK)

    @allure.step("Click On veterinary food")
    def on_click_veterinaryfood(self):
        return self.click(self.VETRINARY_LINK)

    @allure.step("Click On Dental Bones")
    def on_click_dentalbones(self):
        return self.click(self.DENTAL_BONES_LINK)

    @allure.step("Click On Dog poop bags")
    def on_click_dogpoopbags(self):
        return self.click(self.POOPBAGS_LINK)

