"""
Base Test class containing common setup and teardown methods.
"""
import pytest
import io
import logging
import allure
from utils.logger import get_logger
from config.environment import Environment

class BaseTest:
    logger = get_logger()

    @pytest.fixture(scope="function", autouse=True)
    def setup_and_teardown(self, driver, request):
        """
        Setup/teardown fixture. Uses the driver fixture from conftest.py
        """
        self.logger.info(f"--- Starting test: {request.node.name} ---")

        # Capture logs
        log_stream = io.StringIO()
        stream_handler = logging.StreamHandler(log_stream)
        log_format = logging.Formatter('%(asctime)s - [%(levelname)s] - %(message)s')
        stream_handler.setFormatter(log_format)
        self.logger.addHandler(stream_handler)

        self.env = Environment()
        self.driver = driver
        # Make driver available to test class instance explicitly if needed
        request.cls.driver = self.driver

        yield

        # Teardown logic
        with allure.step("Test Teardown"):
            # Logs attachment
            log_content = log_stream.getvalue()
            allure.attach(log_content, name=f"Execution Log for {request.node.name}",
                          attachment_type=allure.attachment_type.TEXT)
            self.logger.removeHandler(stream_handler)
            self.logger.info(f"--- Finished test: {request.node.name} ---")
            # Driver quit is handled by conftest fixture
