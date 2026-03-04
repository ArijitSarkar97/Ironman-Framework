from pages.base_page import BasePage
import allure

class HomepageSearchFunctionality(BasePage):
    SERACH_BAR = ('xpath','//input[@class="search-bar__input"]')
    SEARCH_BUTTON = ('xpath','//button[@class="search-bar__submit"]')


    def __init__(self, driver):
        super().__init__(driver)

    def click_on_search_tab(self):
        self.click(self.SERACH_BAR)

    def enter_search_text(self, search_text):
        self.enter_text(self.SERACH_BAR,search_text)

    def click_search_button(self):
        self.click(self.SEARCH_BUTTON)

