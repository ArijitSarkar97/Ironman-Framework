from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
import allure
import time
import logging

from utils.logger import get_logger

class BasePage:
    """
    BasePage class that contains common methods for all page objects.
    Integrated with Allure steps and custom logging.
    """
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.logger = get_logger(self.__class__.__name__)
    
    def _convert_locator(self, locator):
        """Helper to convert locator tuple/string to (By, value)"""
        if isinstance(locator, tuple): return locator
        
        # If locator came as a custom object or needs mapping (fallback)
        locator_type, locator_value = locator
        locator_map = {
            'id': By.ID,
            'css': By.CSS_SELECTOR,
            'xpath': By.XPATH,
            'name': By.NAME,
            'class_name': By.CLASS_NAME,
            'link_text': By.LINK_TEXT,
            'partial_link_text': By.PARTIAL_LINK_TEXT,
            'tag_name': By.TAG_NAME
        }
        return (locator_map.get(locator_type.lower(), By.ID), locator_value)

    @allure.step("Finding element: {locator}")
    def find_element(self, locator):
        converted_locator = self._convert_locator(locator)
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(converted_locator)
            )
        except TimeoutException:
            self.logger.error(f"Element not found within {self.timeout}s: {locator}")
            raise

    @allure.step("Finding elements: {locator}")
    def find_elements(self, locator):
        converted_locator = self._convert_locator(locator)
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_all_elements_located(converted_locator)
        )

    # --- Actions ---

    @allure.step("Clicking element: {locator}")
    def click(self, locator):
        self.logger.info(f"Clicking element: {locator}")
        try:
            element = self.find_element(locator)
            self.wait_until_clickable(locator)
            element.click()
        except StaleElementReferenceException:
            self.logger.warning(f"StaleElementReferenceException for {locator}, retrying...")
            element = self.find_element(locator)
            element.click()

    @allure.step("Entering text '{text}' into {locator}")
    def enter_text(self, locator, text):
        self.logger.info(f"Entering text '{text}' into {locator}")
        element = self.find_element(locator)
        if element.get_attribute("type") in ["checkbox", "radio"]:
            if str(text).lower() in ["true", "checked", "yes", "1"] and not element.is_selected():
                element.click()
            elif str(text).lower() in ["false", "unchecked", "no", "0"] and element.is_selected():
                element.click()
        else:
            try: element.clear()
            except: pass
            element.send_keys(text)

    @allure.step("Getting text from {locator}")
    def get_text(self, locator):
        text = self.find_element(locator).text
        self.logger.info(f"Got text '{text}' from {locator}")
        return text

    # --- Advanced Interactions ---

    @allure.step("Scrolling to element: {locator}")
    def scroll_to_element(self, locator):
        self.logger.info(f"Scrolling to element: {locator}")
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(0.5) # Allow smooth scroll stability

    @allure.step("Hovering over element: {locator}")
    def hover_over_element(self, locator):
        self.logger.info(f"Hovering over element: {locator}")
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    @allure.step("Double clicking element: {locator}")
    def double_click(self, locator):
        self.logger.info(f"Double clicking element: {locator}")
        element = self.find_element(locator)
        ActionChains(self.driver).double_click(element).perform()

    @allure.step("Right clicking element: {locator}")
    def right_click(self, locator):
        self.logger.info(f"Right clicking element: {locator}")
        element = self.find_element(locator)
        ActionChains(self.driver).context_click(element).perform()

    # --- Waits & States ---

    def wait_until_clickable(self, locator, timeout=None):
        timeout = timeout or self.timeout
        converted_locator = self._convert_locator(locator)
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(converted_locator)
        )

    def is_element_visible(self, locator, timeout=2):
        converted_locator = self._convert_locator(locator)
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(converted_locator)
            )
            return True
        except TimeoutException:
            return False

    # --- Browser Actions ---

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def refresh_page(self):
        self.driver.refresh()

    # --- Dropdowns & Alerts ---

    @allure.step("Selecting '{text}' from dropdown: {locator}")
    def select_dropdown_by_text(self, locator, text):
        self.logger.info(f"Selecting '{text}' from dropdown: {locator}")
        element = self.find_element(locator)
        select = Select(element)
        select.select_by_visible_text(text)

    def switch_to_alert_and_accept(self):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
            self.logger.info("Accepted alert")
        except:
            self.logger.warning("No alert found to accept")




