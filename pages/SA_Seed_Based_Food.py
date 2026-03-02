from pages.base_page import BasePage
import allure
from selenium.webdriver.common.by import By


class SeedBasedFood(BasePage):
    # --- Locators (format: "locator_type", "locator_value") ---
    CLICK_TO_SA = (By.XPATH,"(//a[contains(text(),'Small Animals')])[2]")
    FILTER_DROPDOWN = (By.XPATH,'(//div[@class="collection__filter-group"]/button)[1]')
    CLICK_CHECHBOX = (By.XPATH,'//input[@id="filter.v.availability-1"]')
    SCROLL_DOWN_ELEMENT = (By.XPATH,"//span[text()='Showing 1 - 24 of 30 products']")
    CLICK_IMAGE = (By.XPATH,'(//div[@class="aspect-ratio "]) [1]')
    QUANTITY = (By.XPATH,"//label[text()='Quantity:']")
    CLICK_ADD_TO_CART = (By.XPATH,"(//button[text()='Add to cart'])[1]")
    CLICK_CHECKOUT = (By.XPATH,"//button[text()='Checkout']")
    ENTER_EMAIL = (By.CSS_SELECTOR,"input#email")
    CLICK_EMAIL_ME = (By.CSS_SELECTOR,"input#marketing_opt_in")
    SELECT_BY_COUNTRY = (By.XPATH,'//select[@name="countryCode"]')
    ENTER_FIRST_NAME = (By.XPATH,'//input[@placeholder="First name"]')
    ENTER_LAST_NAME = (By.XPATH,'//input[@placeholder="Last name"]')
    ENTER_ADDRESS = (By.XPATH,'//input[@placeholder="Address"]')
    ENTER_APARTMENT = (By.XPATH,'//input[@placeholder="Address"]')
    ENTER_CITY_NAME = (By.XPATH,'//input[@placeholder="City"]')
    CLICK_STATE = (By.XPATH,'//select[@name="zone"]')
    SELECT_STATE = (By.XPATH,"(//select[@class = 'ZHJU6 _1k3449n7 _1k3449n5 _1fragemzf oAlPg IWR5K tu1VS'])[2]")
    ENTER_PIN_CODE = (By.XPATH,'//input[@placeholder="PIN code"]')
    ENTER_PHONE = (By.XPATH,'//input[@placeholder="Phone"]')
    SAVE_THIS_INFO = (By.XPATH,'(//input[@type="checkbox"])[2]')
    ORANGE_PET_NUTRITION = (By.XPATH,"//h2[text()='Orange Pet Nutrition']")



    def __init__(self, driver):
        super().__init__(driver)

    # --- Actions ---
    # --- Actions ---
    @allure.step("Click small animals")
    def click_small_animals(self):
        return self.click(self.CLICK_TO_SA)

    @allure.step("Select Dropdown")
    def click_filter_dropdown(self):
        return self.click(self.FILTER_DROPDOWN)

    @allure.step("Select CheckBox")
    def select_checkbox(self):
        return self.click(self.CLICK_CHECHBOX)

    @allure.step("Scroll to Product")
    def scroll_to_pet_prod(self):
        return self.scroll_to_element(self.SCROLL_DOWN_ELEMENT)

    @allure.step("Click Product Image")
    def click_product_image(self):
        return self.click(self.CLICK_IMAGE)

    @allure.step("Scroll add to cart")
    def scroll_to_add_to_cart(self):
        return self.scroll_to_element(self.QUANTITY)

    @allure.step("Click add to cart")
    def click_to_add_to_cart(self):
        return self.click(self.CLICK_ADD_TO_CART)

    @allure.step("scroll to checkout")
    def scroll_to_checkout(self):
        return self.scroll_to_element(self.CLICK_CHECKOUT)

    @allure.step("Click Checkout Button")
    def click_checkout_button(self):
        return self.click(self.CLICK_CHECKOUT)

    @allure.step("Enter Email ID")
    def enter_email_ID(self,text):
        return self.enter_text(self.ENTER_EMAIL,text)

    @allure.step("Click email me with news and offers")
    def click_email_me_with_news(self):
        return self.click(self.CLICK_EMAIL_ME)

    @allure.step("Select Delivery by Country")
    def select_by_country(self):
        return self.click(self.SELECT_BY_COUNTRY)

    @allure.step("Enter First Name")
    def enter_first_name(self,text):
        return self.enter_text(self.ENTER_FIRST_NAME,text)

    @allure.step("Enter Last Name")
    def enter_last_name(self,text):
        return self.enter_text(self.ENTER_LAST_NAME,text)

    @allure.step("Enter Address")
    def enter_address(self, text):
        return self.enter_text(self.ENTER_ADDRESS, text)

    @allure.step("Enter Address")
    def enter_apartment(self, text):
        return self.enter_text(self.ENTER_APARTMENT, text)

    @allure.step("Enter City Name")
    def enter_city(self,text):
        return self.enter_text(self.ENTER_CITY_NAME, text)

    @allure.step("Scroll to State")
    def scroll_to_state(self):
        return self.scroll_to_element(self.CLICK_STATE)

    @allure.step("Click State")
    def click_state(self):
        return self.click(self.CLICK_STATE)

    @allure.step("Enter State")
    def select_state(self,text):
        return self.select_dropdown_by_text(self.SELECT_STATE,text)

    @allure.step("Enter PINCODE")
    def enter_PINCODE(self,text):
        return self.enter_text(self.ENTER_PIN_CODE,text)

    @allure.step("Enter Phone")
    def enter_phone(self,text):
        return self.enter_text(self.ENTER_PHONE,text)

    @allure.step("Save Info")
    def click_save_info(self):
        return self.click(self.SAVE_THIS_INFO)


















