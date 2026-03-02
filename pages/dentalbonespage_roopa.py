from pages.base_page import BasePage
import allure

class DentalBonesPage(BasePage):
    HOMEPAGE_LINK = ("xpath","//a[.='Go to Homepage']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("go back to homepage")
    def on_click_backtohomepage(self):
        return self.click(self.HOMEPAGE_LINK)
