import pytest
from selenium import webdriver
from automation.test_data.env import *
from automation.src.common import common

def get_webdriver(browser):
    driver = None
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=chrome_driver_path)
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver


@pytest.fixture(scope="session")
def setup():
    driver = get_webdriver(browser_setup)
    obj = common(driver)
    obj.launch_url(url)
    return obj