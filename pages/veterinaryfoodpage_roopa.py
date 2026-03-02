from pages.base_page import BasePage
import allure

class VeterinaryFoodPage(BasePage):
    AVAILABILITY_FILTER = ("xpath","//button[contains(.,'Availability')]")
    IN_STOCK_CHECKBOX = ("xpath","//label[@for='filter.v.availability-1']")
    SCROLL_ELEMENT = ("xpath","//div[@class='product-item product-item--vertical  1/3--tablet-and-up 1/4--desk']")
    FIRST_PRODUCT = ("xpath","//div[@class='product-item product-item--vertical  1/3--tablet-and-up 1/4--desk']")
    ENQUIRE_LINK = ("xpath","//a[.='Enquire about this Product']")
    NAME_TEXTBOX = ("id","contact-form-name")
    EMAIL_TEXTBOX = ("id","contact-form-email")
    MOBILE_TEXTBOX = ("id","contact-form-mobile")
    LOCATION_TEXTBOX = ("id","contact-form-location")



    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Apply filter")
    def on_click_availability(self):
        return self.click(self.AVAILABILITY_FILTER)

    @allure.step("Apply filter")
    def on_click_instock(self):
        return self.click(self.IN_STOCK_CHECKBOX)

    # @allure.step("Scroll to an element")
    # def scroll_action(self):
    #     return self.scroll_to_element(self.SCROLL_ELEMENT)

    def select_product(self):
        return self.click(self.FIRST_PRODUCT)

    def on_click_enquire(self):
        return self.click(self.ENQUIRE_LINK)

    def enter_contact_name(self,name):
        return self.enter_text(self.NAME_TEXTBOX,name)

    def enter_contact_email(self,email):
        return self.enter_text(self.EMAIL_TEXTBOX,email)

    def enter_contact_mobile(self,mobile):
        return self.enter_text(self.MOBILE_TEXTBOX,mobile)

    def enter_contact_location(self,location):
        return self.enter_text(self.LOCATION_TEXTBOX,location)


