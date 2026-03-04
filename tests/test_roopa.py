import pytest
import allure

from tests.base_test import BaseTest
from pages.homepage_roopa import HomePage

from pages.veterinaryfoodpage_roopa import VeterinaryFoodPage
from pages.dentalbonespage_roopa import DentalBonesPage
from pages.dogpoopbags_roopa import DogPoopBags
from utils.data_reader import get_excel_data

@allure.epic("pytest-automation")
@allure.feature("orangepetpractice")
class TestOrangePetPage(BaseTest):

    file_path = r"test-data\contact_details.xlsx"
    sheet_name = "contact_details"

    test_data = get_excel_data(file_path, sheet_name)
    @pytest.mark.parametrize("name,email,mobile,location",test_data)
    def test_automation_orangepet(self, driver, config,name,email,mobile,location):

        homepage = HomePage(driver)

        veterinarypage = VeterinaryFoodPage(driver)
        dentalbonespage = DentalBonesPage(driver)
        dogpoopbagpage = DogPoopBags(driver)

        driver.get(config.get('environments', {}).get('orangepet_roopa', {}).get('base_url', ''))

        # with allure.step(f"1. on click My Account \n"):
        #     homepage.on_click_myaccount()
        #     self.logger.info("successfull")
        #
        # with allure.step(f"2.Fill email_input with valid data \n"):
        #     loginpage.fill_email_input("roops_reddy@yahoo.com")
        #     self.logger.info("Fill email_input with valid data executed successfully")
        #
        # with allure.step(f"2.Fill password_input with valid data \n"):
        #     loginpage.fill_password_input("Tanvi@2446")
        #     self.logger.info("Fill password_input with valid data executed successfully")

        # with allure.step(f"3. on click Login button \n"):
        #     loginpage.click_login_button()
        #
        #     self.logger.info("successfull")

        with allure.step(f"mouse hover dogs link \n"):
            homepage.mouse_hover_dogs()
            self.logger.info("successful")

        with allure.step(f"select veterinary food under dogs \n"):
            homepage.on_click_veterinaryfood()
            self.logger.info("Successful")

        with allure.step(f"check availability"):
            veterinarypage.on_click_availability()
            self.logger.info("successful")

        with allure.step(f"apply filter instock"):
            veterinarypage.on_click_instock()
            self.logger.info("successful")

        with allure.step(f"selecting product"):
            veterinarypage.select_product()
            self.logger.info("product selected")

        with allure.step(f"clicking for enquiry form"):
            veterinarypage.on_click_enquire()
            self.logger.info("success")

        with allure.step(f"enter contact name"):
            veterinarypage.enter_contact_name(name)
            self.logger.info("enter name with valid data successful")

        with allure.step(f"enter contact email"):
            veterinarypage.enter_contact_email(email)
            self.logger.info("enter email with valid data successful")

        with allure.step(f"enter contact mobile"):
            veterinarypage.enter_contact_mobile(mobile)
            self.logger.info("enter mobile with valid data successful")

        with allure.step(f"enter contact location"):
            veterinarypage.enter_contact_location(location)
            self.logger.info("enter location with valid data successful")

        with allure.step(f"mouse hover dogs link \n"):
            homepage.mouse_hover_dogs()
            self.logger.info("successful")

        with allure.step(f"select dental bones under dogs"):
            homepage.on_click_dentalbones()
            self.logger.info("successful")

        with allure.step(f"navigate to homepage"):
            dentalbonespage.on_click_backtohomepage()
            self.logger.info("successful")

        with allure.step(f"mouse hover dogs link \n"):
            homepage.mouse_hover_dogs()
            self.logger.info("successful")

        with allure.step(f"select dog poop bags under dogs"):
            homepage.on_click_dogpoopbags()
            self.logger.info("successful")

        with allure.step(f"select for product"):
            dogpoopbagpage.select_product()
            self.logger.info("product selection successful")


        with allure.step(f"add to product to cart"):
            dogpoopbagpage.add_to_cart()
            self.logger.info("product added to cart successful")







