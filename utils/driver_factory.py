
from selenium import webdriver

def get_driver(browser="chrome", headless=True):
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")
        return webdriver.Chrome(options=options)
    raise ValueError(f"Browser {browser} not supported in this factory yet.")
