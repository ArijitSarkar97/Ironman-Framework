import pytest
import io
import logging
import allure
from selenium.webdriver.common.by import By
from pages._malini import HomePage
from pages.contact_page_malini import ContactPage
from utils.logger import get_logger
from config.environment import Environment


class BaseTest:
    logger = get_logger("BaseTest")

    @pytest.fixture(scope="function", autouse=True)
    def setup_and_teardown(self, driver, request):



        self.logger.info(f"--- Starting test: {request.node.name} ---")


        log_stream = io.StringIO()
        stream_handler = logging.StreamHandler(log_stream)
        log_format = logging.Formatter('%(asctime)s - [%(levelname)s] - %(message)s')
        stream_handler.setFormatter(log_format)
        self.logger.addHandler(stream_handler)


        self.env = Environment()
        self.driver = driver
        request.cls.driver = self.driver

        yield


        with allure.step("Test Teardown"):
            log_content = log_stream.getvalue()
            allure.attach(
                log_content,
                name=f"Execution Log for {request.node.name}",
                attachment_type=allure.attachment_type.TEXT
            )
            self.logger.removeHandler(stream_handler)
            self.logger.info(f"--- Finished test: {request.node.name} ---")
        # driver quit handled by conftest.py fixture


@pytest.mark.usefixtures("setup_and_teardown")
class TestContactForm(BaseTest):

    def test_contact_form_submission(self):
        """
        Open website → Navigate to Contact → Fill the form → Submit → Verify success message
        """
        self.driver.get("https://www.orangepet.in/")

        home = HomePage(self.driver)
        contact = ContactPage(self.driver)
        home.hover_over_element((By.LINK_TEXT, "Contact"))
        home.click((By.LINK_TEXT, "Contact"))

        # Fill the contact form
        contact.fill_name("Test User")
        contact.fill_email("testuser@example.com")
        contact.fill_phone("9876543210")
        contact.fill_location("Bangalore")
        contact.select_enquire_about("Cat Food")  # dropdown selection
        contact.fill_message("This is a test message from automation.")


        contact.submit_form()


