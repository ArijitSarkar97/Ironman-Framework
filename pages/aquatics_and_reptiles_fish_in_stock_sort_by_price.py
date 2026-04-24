from pages.base_page import BasePage
import allure

class AquaticsandReptilesfiler(BasePage):
    HOME_PAGE_TEXT = ('xpath','(//a[text()= "Home"])[2]')
    AQUATICS_AND_REPTILES = ("xpath",'(//a[text()="Aquatics & Reptiles"])[2]')
    FISH = ('xpath','(//a[text()="Fish"])[2]')
    AVALIBILITY_FILTER = ('xpath','//button[text()="Availability"]')
    IN_STOCK_ELEMENT = ('xpath','//label[contains(text(),"In stock")]')
    AQUATICS_AND_REPTILES_DROPDOWN = ('id','desktop-menu-0-7')
    SORT_BY = ('xpath','//span[text()="Sort by: Featured"]')
    PRICE_LOW_TO_HIGH = ('xpath','//button[contains(text(),"Price, low to high")]')
    FIRST_PRODUCT_PRICE = ('xpath','//span[text()="From Rs. 175.00"]')
    SECOND_PRODUCT_PRICE = ('xpath','//span[text()="From Rs. 250.00"]')


    def __init__(self, driver):
        super().__init__(driver)

    # @allure.step('Navigation to home is sucessfull')

    @allure.step("Get home_a text")
    def get_home_a_text(self):
        return self.get_text(self.HOME_PAGE_TEXT)

    @allure.step("hover over Aquatics & Reptiles")
    def hover_over_aquatics_and_reptiles(self):
        self.hover_over_element(self.AQUATICS_AND_REPTILES)
        self.get_text(self.AQUATICS_AND_REPTILES_DROPDOWN)

    @allure.step("CLick on the fish dropdown")
    def click_on_fish(self):
        self.click(self.FISH)

    @allure.step("Clicking element is sucessfull")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("click on Avalibility element")
    def click_on_avalibility_element(self):
        self.click(self.AVALIBILITY_FILTER)
        self.click(self.IN_STOCK_ELEMENT)

    @allure.step("scroll to element sort by feature")
    def scroll_to_sort_by_feature(self):
        self.scroll_to_element(self.SORT_BY)

    @allure.step("click on sort by feature")
    def click_on_sort_by(self):
        self.click(self.SORT_BY)

    @allure.step("click on sort by feature price low to high")
    def click_on_sort_by_price_low_to_high(self):
        self.click(self.PRICE_LOW_TO_HIGH)

    @allure.step("Get price for the first product")
    def get_first_product_price(self):
        price1 = self.get_text(self.FIRST_PRODUCT_PRICE)
        amount1 = price1.split("Rs. ")[1]
        return amount1

    @allure.step("Get price for the second product")
    def get_second_product_price(self):
        price2 = self.get_text(self.SECOND_PRODUCT_PRICE)
        amount2 = price2.split("Rs. ")[1]
        return amount2







