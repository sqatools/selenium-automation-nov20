import pytest
from selenium import webdriver


driver = webdriver.Chrome()

@pytest.fixture(scope="session")
def setup():
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.calculator.net/mortgage-calculator.html")
    return driver


@pytest.fixture(scope="session")
def teardown():
    yield
    driver.close()