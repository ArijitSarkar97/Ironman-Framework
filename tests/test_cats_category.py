import pytest
import io
import logging
import allure
from pages.home_page_malini  import HomePage
from pages.cats_page_malini import CatsPage
from pages.product_page_malini import ProductPage
from pages.cart_page_malini import CartPage
from pages.checkout_page_malini import CheckoutPage
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
            allure.attach(log_content, name=f"Execution Log for {request.node.name}",
                          attachment_type=allure.attachment_type.TEXT)
            self.logger.removeHandler(stream_handler)
            self.logger.info(f"--- Finished test: {request.node.name} ---")

@pytest.mark.usefixtures("setup_and_teardown")
class TestCatsFlow(BaseTest):

    def test_cats_end_to_end(self):
        """
        Open website → Cats page → Add first product to cart → Checkout → Verify checkout page
        """
        self.driver.get("https://www.orangepet.in/")

        home = HomePage(self.driver)
        cats = CatsPage(self.driver)
        product = ProductPage(self.driver)
        cart = CartPage(self.driver)
        checkout = CheckoutPage(self.driver)


        home.open_cats_page()
        cats.open_first_product()
        product.add_to_cart()
        cart.open_cart()
        cart.click_checkout()

        assert checkout.is_checkout_loaded(), "Checkout page did not load"