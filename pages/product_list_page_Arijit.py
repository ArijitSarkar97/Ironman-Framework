from time import sleep

from pages.base_page import BasePage
import allure

class OrangePetProductListPage(BasePage):
    AVAILABILITY_FILTER=("xpath","//button[contains(text(),'Availability')]")
    IN_STOCK=("id","filter.v.availability-1")
    PRODUCTS= ("xpath", "//div[@class='product-item__info-inner']/a[2]")
    LOGIN_BUTTON=("xpath","//button[contains(text(),'Login')]")
    DOG_MODULE=("xpath","(//a[contains(text(),'Dogs')])[2]")
    DOG_DRY_FOOD=("xpath","(//a[@href='/collections/dry-dog-food'])[2]")
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Hover to dog")
    def click_on_in_stock(self):
        self.click(self.AVAILABILITY_FILTER)
        self.click(self.IN_STOCK)

    @allure.step("Get all the products")
    def get_all_product(self):
        return self.find_elements(self.PRODUCTS)
        for i in range(len(products)):
            products[i].click()


    # @allure.step("Click on dog dry food")
    # def click_on_dog_dryfood(self):
    #     self.click(self.DOG_DRY_FOOD)

