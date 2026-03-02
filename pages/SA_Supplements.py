from pages.base_page import BasePage
import allure
from selenium.webdriver.common.by import By


class Supplements(BasePage):
    # --- Locators (format: "locator_type", "locator_value") ---

    CLICK_SUPPLEMENTS = (By.XPATH,'(//a[@href="/collections/small-animals-feed-supplements"])[2]')
    SCROLL_DOWN_TO_SUPPLEMENTS = (By.XPATH,"//span[text()='Showing 1 - 15 of 15 products']")


    # ORANGE_PET_NUTRITION = (By.XPATH,'//a[@href="https://www.orangepet.in"]')
    # HOVER_OVER_SA = (By.XPATH,'(//a[@href="/collections/small-animals"])[2]')
    # SELECT_PALLETED_FOOD = (By.XPATH,'(//a[@href="/collections/small-animals-pelleted-food"])[2]')
    # SCROLL_DOWN_ELEMENT = (By.XPATH, "//span[text()='Showing 1 - 12 of 12 products']")


    # CLICK_TO_SA = (By.XPATH,"(//a[contains(text(),'Small Animals')])[2]")
    # FILTER_DROPDOWN = (By.XPATH,'(//div[@class="collection__filter-group"]/button)[1]')
    # CLICK_CHECHBOX = (By.XPATH,'//input[@id="filter.v.availability-1"]')
    # SCROLL_DOWN_ELEMENT = (By.XPATH,"//span[text()='Showing 1 - 24 of 30 products']")
    # CLICK_IMAGE = (By.XPATH,'(//div[@class="aspect-ratio "]) [1]')
    # QUANTITY = (By.XPATH,"//label[text()='Quantity:']")
    # CLICK_ADD_TO_CART = (By.XPATH,"(//button[text()='Add to cart'])[1]")
    # CLICK_CHECKOUT = (By.XPATH,"//button[text()='Checkout']")
    # ENTER_EMAIL = (By.CSS_SELECTOR,"input#email")
    # CLICK_EMAIL_ME = (By.CSS_SELECTOR,"input#marketing_opt_in")
    # SELECT_BY_COUNTRY = (By.XPATH,'//select[@name="countryCode"]')
    # ENTER_FIRST_NAME = (By.XPATH,'//input[@placeholder="First name"]')
    # ENTER_LAST_NAME = (By.XPATH,'//input[@placeholder="Last name"]')
    # ENTER_ADDRESS = (By.XPATH,'//input[@placeholder="Address"]')
    # ENTER_APARTMENT = (By.XPATH,'//input[@placeholder="Address"]')
    # ENTER_CITY_NAME = (By.XPATH,'//input[@placeholder="City"]')
    # CLICK_STATE = (By.XPATH,'//select[@name="zone"]')
    # SELECT_STATE = (By.XPATH,"(//select[@class = 'ZHJU6 _1k3449n7 _1k3449n5 _1fragemzf oAlPg IWR5K tu1VS'])[2]")
    # ENTER_PIN_CODE = (By.XPATH,'//input[@placeholder="PIN code"]')
    # ENTER_PHONE = (By.XPATH,'//input[@placeholder="Phone"]')
    # SAVE_THIS_INFO = (By.XPATH,'(//input[@type="checkbox"])[2]')


    def __init__(self, driver):
        super().__init__(driver)

    # --- Actions ---
    # --- Actions ---

    @allure.step("Click Orange")
    def click_supplements(self):
        return self.click(self.CLICK_SUPPLEMENTS)

    # @allure.step("Click Orange")
    # def click_orange_text(self):
    #     return self.click(self.ORANGE_PET_NUTRITION)
    #
    # @allure.step("Hover to small animals")
    # def hover_to_small_animals(self):
    #     return self.hover_over_element(self.HOVER_OVER_SA)
    #
    # @allure.step("Select Palleted Food")
    # def select_palleted_food(self):
    #     return self.click(self.SELECT_PALLETED_FOOD)
    #
    @allure.step("Scroll to Product")
    def scroll_to_supplements(self):
        return self.scroll_to_element(self.SCROLL_DOWN_TO_SUPPLEMENTS)

























