import pytest
import json
import os
import logging
import allure
from colorlog import ColoredFormatter
from selenium import webdriver

# --- Logging Setup with ColorLog ---
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    formatter = ColoredFormatter(
        "%(log_color)s%(levelname)-8s%(reset)s %(white)s%(message)s",
        datefmt=None,
        reset=True,
        log_colors={
            'DEBUG':    'cyan',
            'INFO':     'green',
            'WARNING':  'yellow',
            'ERROR':    'red',
            'CRITICAL': 'red,bg_white',
        },
        secondary_log_colors={},
        style='%'
    )
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    
    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=None, help="Browser to run tests on (chrome, firefox, edge)")
    parser.addoption("--headless", action="store_true", default=None, help="Run tests in headless mode")

@pytest.fixture(scope="session")
def config():
    import yaml
    config_path = os.path.join(os.path.dirname(__file__), 'config', 'config.yaml')
    with open(config_path) as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="function")
def driver(request, config):
    # Determine browser: either from CLI param, fixture param, or config file
    cli_browser = request.config.getoption("--browser")
    browser = cli_browser if cli_browser else (request.param if hasattr(request, 'param') else config.get('browser', {}).get('default', 'chrome'))
    if not browser:
        browser = 'chrome'
    browser = browser.lower()
    
    cli_headless = request.config.getoption("--headless")
    headless = True if cli_headless else config.get('browser', {}).get('headless', False)
    
    driver = None
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")  # Chrome 112+ requires --headless=new
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
        # Add common options to avoid issues
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-extensions")
        try:
            driver = webdriver.Chrome(options=options)
        except Exception as e:
            raise RuntimeError(
                f"Failed to start Chrome. Make sure Google Chrome is installed.\n"
                f"Error: {e}"
            )
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless: options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    elif browser == "edge":
        options = webdriver.EdgeOptions()
        if headless: options.add_argument("--headless=new")
        driver = webdriver.Edge(options=options)
    else:
        raise Exception(f"Browser {browser} not supported")

    driver.maximize_window()
    if 'implicit_wait' in config['browser']:
        driver.implicitly_wait(config['browser']['implicit_wait'])
    
    yield driver
    
    if driver:
        driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Capture screenshot on failure and attach to Allure
    """
    outcome = yield
    report = outcome.get_result()
    
    if report.when == 'call' and report.failed:
        if "driver" in item.funcargs:
            driver = item.funcargs["driver"]
            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"failure_{item.name}",
                attachment_type=allure.attachment_type.PNG
            )
