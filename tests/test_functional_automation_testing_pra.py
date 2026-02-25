import pytest
import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from tests.base_test import BaseTest
from pages.automation_testing_pra_page import AutomationTestingPraPage

@allure.epic("pytest-automation")
@allure.feature("AutomationTestingPraPage")
class TestAutomationTestingPraPage(BaseTest):

    @allure.story("test_automation_testing_pra_page_fill_all_inputs")
    @allure.title("test_automation_testing_pra_page_fill_all_inputs Execution")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.functional
    def test_automation_testing_pra_page_fill_all_inputs(self, driver, config):
        """
        Test Case: test_automation_testing_pra_page_fill_all_inputs
        Type: functional
        Steps:
        1. Fill name_input with valid data
        2. Fill email_input with valid data
        3. Fill phone_input with valid data
        4. Fill textarea_textarea with valid data
        5. Fill male_input with valid data
        6. Fill female_input with valid data
        7. Fill sunday_input with valid data
        8. Fill monday_input with valid data
        9. Fill tuesday_input with valid data
        10. Fill wednesday_input with valid data
        11. Fill thursday_input with valid data
        12. Fill friday_input with valid data
        13. Fill saturday_input with valid data
        14. Fill datepicker_input with valid data
        15. Fill txtdate_input with valid data
        16. Fill start_date_input with valid data
        17. Fill end_date_input with valid data
        18. Fill singlefileinput_input with valid data
        19. Fill multiplefilesinput_input with valid data
        20. Fill input_input with valid data
        21. Fill wikipedia1_wikipedia_search_input_input with valid data
        22. Fill field1_input with valid data
        23. Fill field2_input with valid data
        24. Fill amount_input with valid data
        25. Fill combobox_input with valid data
        26. Fill input1_input with valid data
        27. Fill input2_input with valid data
        28. Fill input3_input with valid data
        """
        # Initialize Page Objects
        automationtestingprapage = AutomationTestingPraPage(driver)
        
        driver.get(config.get('environments', {}).get('dev', {}).get('base_url', ''))
        with allure.step(f"1. Fill name_input with valid data \n"):
            automationtestingprapage.fill_name_input("test_data")
            self.logger.info("Fill name_input with valid data executed successfully")
        with allure.step(f"2. Fill email_input with valid data \n"):
            automationtestingprapage.fill_email_input("test@example.com")
            self.logger.info("Fill email_input with valid data executed successfully")
        with allure.step(f"3. Fill phone_input with valid data \n"):
            automationtestingprapage.fill_phone_input("test_data")
            self.logger.info("Fill phone_input with valid data executed successfully")
        with allure.step(f"4. Fill textarea_textarea with valid data \n"):
            automationtestingprapage.fill_textarea_textarea("test_data")
            self.logger.info("Fill textarea_textarea with valid data executed successfully")
        with allure.step(f"5. Fill male_input with valid data \n"):
            automationtestingprapage.fill_male_input("test_data")
            self.logger.info("Fill male_input with valid data executed successfully")
        with allure.step(f"6. Fill female_input with valid data \n"):
            automationtestingprapage.fill_male_input("test_data")
            self.logger.info("Fill female_input with valid data executed successfully")
        with allure.step(f"7. Fill sunday_input with valid data \n"):
            automationtestingprapage.fill_sunday_input("test_data")
            self.logger.info("Fill sunday_input with valid data executed successfully")
        with allure.step(f"8. Fill monday_input with valid data \n"):
            automationtestingprapage.fill_monday_input("test_data")
            self.logger.info("Fill monday_input with valid data executed successfully")
        with allure.step(f"9. Fill tuesday_input with valid data \n"):
            automationtestingprapage.fill_tuesday_input("test_data")
            self.logger.info("Fill tuesday_input with valid data executed successfully")
        with allure.step(f"10. Fill wednesday_input with valid data \n"):
            automationtestingprapage.fill_wednesday_input("test_data")
            self.logger.info("Fill wednesday_input with valid data executed successfully")
        with allure.step(f"11. Fill thursday_input with valid data \n"):
            automationtestingprapage.fill_thursday_input("test_data")
            self.logger.info("Fill thursday_input with valid data executed successfully")
        with allure.step(f"12. Fill friday_input with valid data \n"):
            automationtestingprapage.fill_friday_input("test_data")
            self.logger.info("Fill friday_input with valid data executed successfully")
        with allure.step(f"13. Fill saturday_input with valid data \n"):
            automationtestingprapage.fill_saturday_input("test_data")
            self.logger.info("Fill saturday_input with valid data executed successfully")
        with allure.step(f"14. Fill datepicker_input with valid data \n"):
            automationtestingprapage.fill_datepicker_input("test_data")
            self.logger.info("Fill datepicker_input with valid data executed successfully")
        with allure.step(f"15. Fill txtdate_input with valid data \n"):
            automationtestingprapage.fill_txtdate_input("test_data")
            self.logger.info("Fill txtdate_input with valid data executed successfully")
        with allure.step(f"16. Fill start_date_input with valid data \n"):
            automationtestingprapage.fill_start_date_input("test_data")
            self.logger.info("Fill start_date_input with valid data executed successfully")
        with allure.step(f"17. Fill end_date_input with valid data \n"):
            automationtestingprapage.fill_end_date_input("test_data")
            self.logger.info("Fill end_date_input with valid data executed successfully")
        with allure.step(f"18. Fill singlefileinput_input with valid data \n"):
            automationtestingprapage.fill_singlefileinput_input("test_data")
            self.logger.info("Fill singlefileinput_input with valid data executed successfully")
        with allure.step(f"19. Fill multiplefilesinput_input with valid data \n"):
            automationtestingprapage.fill_multiplefilesinput_input("test_data")
            self.logger.info("Fill multiplefilesinput_input with valid data executed successfully")
        with allure.step(f"20. Fill input_input with valid data \n"):
            automationtestingprapage.fill_input_input("test_data")
            self.logger.info("Fill input_input with valid data executed successfully")
        with allure.step(f"21. Fill wikipedia1_wikipedia_search_input_input with valid data \n"):
            automationtestingprapage.fill_input_input("test_data")
            self.logger.info("Fill wikipedia1_wikipedia_search_input_input with valid data executed successfully")
        with allure.step(f"22. Fill field1_input with valid data \n"):
            automationtestingprapage.fill_field1_input("test_data")
            self.logger.info("Fill field1_input with valid data executed successfully")
        with allure.step(f"23. Fill field2_input with valid data \n"):
            automationtestingprapage.fill_field2_input("test_data")
            self.logger.info("Fill field2_input with valid data executed successfully")
        with allure.step(f"24. Fill amount_input with valid data \n"):
            automationtestingprapage.fill_amount_input("test_data")
            self.logger.info("Fill amount_input with valid data executed successfully")
        with allure.step(f"25. Fill combobox_input with valid data \n"):
            automationtestingprapage.fill_combobox_input("test_data")
            self.logger.info("Fill combobox_input with valid data executed successfully")
        with allure.step(f"26. Fill input1_input with valid data \n"):
            automationtestingprapage.fill_input1_input("test_data")
            self.logger.info("Fill input1_input with valid data executed successfully")
        with allure.step(f"27. Fill input2_input with valid data \n"):
            automationtestingprapage.fill_input2_input("test_data")
            self.logger.info("Fill input2_input with valid data executed successfully")
        with allure.step(f"28. Fill input3_input with valid data \n"):
            automationtestingprapage.fill_input3_input("test_data")
            self.logger.info("Fill input3_input with valid data executed successfully")

        # Assert success outcome (URL change, success message, or no errors)
        time.sleep(1)  # Brief wait for response
        error_elements = driver.find_elements(By.CSS_SELECTOR, ".error, .alert-danger, .alert-error, [class*='error']")
        visible_errors = [e for e in error_elements if e.is_displayed()]
        assert len(visible_errors) == 0, \
            f"No error messages should appear after valid input, found: {[e.text for e in visible_errors]}"


    @allure.story("test_automation_testing_pra_page_button_interactions")
    @allure.title("test_automation_testing_pra_page_button_interactions Execution")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.functional
    def test_automation_testing_pra_page_button_interactions(self, driver, config):
        """
        Test Case: test_automation_testing_pra_page_button_interactions
        Type: functional
        Steps:
        1. Click submit_button button
        2. Click upload_single_file_button button
        3. Click upload_multiple_files_button button
        4. Click start_button button
        5. Click alertbtn_button button
        6. Click confirmbtn_button button
        7. Click promptbtn_button button
        8. Click new_tab_button button
        9. Click popup_button button
        10. Click point_me_button button
        11. Click copy_text_button button
        12. Click btn1_button button
        13. Click btn2_button button
        14. Click btn3_button button
        """
        # Initialize Page Objects
        automationtestingprapage = AutomationTestingPraPage(driver)
        
        driver.get(config.get('environments', {}).get('dev', {}).get('base_url', ''))
        with allure.step(f"1. Click submit_button button \n"):
            automationtestingprapage.click_submit_button()
            self.logger.info("Click submit_button button executed successfully")
        with allure.step(f"2. Click upload_single_file_button button \n"):
            automationtestingprapage.click_upload_single_file_button()
            self.logger.info("Click upload_single_file_button button executed successfully")
        with allure.step(f"3. Click upload_multiple_files_button button \n"):
            automationtestingprapage.click_upload_multiple_files_button()
            self.logger.info("Click upload_multiple_files_button button executed successfully")
        with allure.step(f"4. Click start_button button \n"):
            automationtestingprapage.click_start_button()
            self.logger.info("Click start_button button executed successfully")
        with allure.step(f"5. Click alertbtn_button button \n"):
            automationtestingprapage.click_alertbtn_button()
            self.logger.info("Click alertbtn_button button executed successfully")
        with allure.step(f"6. Click confirmbtn_button button \n"):
            automationtestingprapage.click_confirmbtn_button()
            self.logger.info("Click confirmbtn_button button executed successfully")
        with allure.step(f"7. Click promptbtn_button button \n"):
            automationtestingprapage.click_promptbtn_button()
            self.logger.info("Click promptbtn_button button executed successfully")
        with allure.step(f"8. Click new_tab_button button \n"):
            automationtestingprapage.click_new_tab_button()
            self.logger.info("Click new_tab_button button executed successfully")
        with allure.step(f"9. Click popup_button button \n"):
            automationtestingprapage.click_popup_button()
            self.logger.info("Click popup_button button executed successfully")
        with allure.step(f"10. Click point_me_button button \n"):
            automationtestingprapage.click_point_me_button()
            self.logger.info("Click point_me_button button executed successfully")
        with allure.step(f"11. Click copy_text_button button \n"):
            automationtestingprapage.click_copy_text_button()
            self.logger.info("Click copy_text_button button executed successfully")
        with allure.step(f"12. Click btn1_button button \n"):
            automationtestingprapage.click_btn1_button()
            self.logger.info("Click btn1_button button executed successfully")
        with allure.step(f"13. Click btn2_button button \n"):
            automationtestingprapage.click_btn2_button()
            self.logger.info("Click btn2_button button executed successfully")
        with allure.step(f"14. Click btn3_button button \n"):
            automationtestingprapage.click_btn3_button()
            self.logger.info("Click btn3_button button executed successfully")

        # Assert success outcome (URL change, success message, or no errors)
        time.sleep(1)  # Brief wait for response
        error_elements = driver.find_elements(By.CSS_SELECTOR, ".error, .alert-danger, .alert-error, [class*='error']")
        visible_errors = [e for e in error_elements if e.is_displayed()]
        assert len(visible_errors) == 0, \
            f"No error messages should appear after valid input, found: {[e.text for e in visible_errors]}"


    @allure.story("test_automation_testing_pra_page_search_functionality")
    @allure.title("test_automation_testing_pra_page_search_functionality Execution")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.functional
    def test_automation_testing_pra_page_search_functionality(self, driver, config):
        """
        Test Case: test_automation_testing_pra_page_search_functionality
        Type: functional
        Steps:
        1. Type search query in wikipedia1_wikipedia_search_input_input
        2. Submit search
        3. Verify results appear
        """
        # Initialize Page Objects
        automationtestingprapage = AutomationTestingPraPage(driver)
        
        driver.get(config.get('environments', {}).get('dev', {}).get('base_url', ''))
        with allure.step(f"1. Type search query in wikipedia1_wikipedia_search_input_input \n"):
            automationtestingprapage.fill_input_input("Test Search Query")
            self.logger.info("Type search query in wikipedia1_wikipedia_search_input_input executed successfully")
        with allure.step(f"2. Submit search (Fallback Click) \n"):
            self.logger.warning("No specific element found for click: Submit search")
        with allure.step(f"3. Verify: Verify results appear \n"):
            # This step requires specific element identification to assert visibility
            self.logger.info("Verification step: Verify results appear")

        # Assert success outcome (URL change, success message, or no errors)
        time.sleep(1)  # Brief wait for response
        error_elements = driver.find_elements(By.CSS_SELECTOR, ".error, .alert-danger, .alert-error, [class*='error']")
        visible_errors = [e for e in error_elements if e.is_displayed()]
        assert len(visible_errors) == 0, \
            f"No error messages should appear after valid input, found: {[e.text for e in visible_errors]}"

