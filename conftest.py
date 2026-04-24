import pytest
import json
import os
import logging
import allure
import threading
import uvicorn
import time
from colorlog import ColoredFormatter
from selenium import webdriver
from mock_server.main import app
from api_clients.auth_client import AuthClient

# --- Logging Setup with ColorLog ---
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Set environment variable early for the Environment class
    env_name = config.getoption("--env", default="orange_pet")
    os.environ['ENV'] = env_name

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
    parser.addoption("--env", action="store", default="orange_pet", help="Environment to run tests on (dev, staging, prod, orange_pet, mock)")

@pytest.fixture(scope="session")
def config(request):
    import yaml
    config_path = os.path.join(os.path.dirname(__file__), 'config', 'config.yaml')
    with open(config_path) as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="session", autouse=True)
def run_mock_server(request):
    """Starts the mock server if the environment is set to 'mock'."""
    env = request.config.getoption("--env")
    if env == "mock":
        # Start uvicorn in a separate thread
        config = uvicorn.Config(app, host="127.0.0.1", port=8000, log_level="info")
        server = uvicorn.Server(config)
        thread = threading.Thread(target=server.run, daemon=True)
        thread.start()
        
        # Give the server a moment to start
        time.sleep(1)
        logging.info("Mock Server started at http://127.0.0.1:8000")
        
        yield
        
        # Shutdown server
        server.should_exit = True
        thread.join(timeout=2)
    else:
        yield

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
        # Remove "Chrome is being controlled by automated test software"
        options.add_experimental_option("excludeSwitches", ["enable-automation"])

        # Disable automation extension
        options.add_experimental_option("useAutomationExtension", False)

        # Disable blink automation flag
        options.add_argument("--disable-blink-features=AutomationControlled")

        options.page_load_strategy = 'eager'
        try:
            driver = webdriver.Chrome(options=options)
            # Remove webdriver property
            driver.execute_script(
                "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
            )
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

@pytest.fixture(scope="session")
def auth_api(request):
    """Fixture to provide AuthAPI client."""
    env_name = request.config.getoption("--env")
    return AuthClient(env_name=env_name)

@pytest.fixture(scope="function")
def api_authenticated_driver(driver, auth_api, config):
    """
    Hybrid Fixture: 
    1. Logs in via API.
    2. Injects token into browser.
    3. Returns the driver ready for UI actions.
    """
    # 1. Get token via API
    token = auth_api.get_token("admin", "password")
    
    if token:
        # 2. Open base URL first (Selenium needs to be on the domain to set cookies)
        driver.get(config['environments'][os.getenv('ENV')]['base_url'])
        
        # 3. Inject token as a cookie
        driver.add_cookie({
            "name": "auth_token",
            "value": token,
            "path": "/"
        })
        
        # 4. Refresh to apply the session
        driver.refresh()
        logging.info("Successfully injected API token into browser session.")
    
    return driver

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
