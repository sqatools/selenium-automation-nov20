import pytest
from selenium import webdriver
from time import sleep

@pytest.fixture(scope="function")
# This will execute for each each test cases
#@pytest.fixture(scope="module")
# This will
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

def test_first_case(setup):
    setup.get("https://www.sqatools.in/p/home.html")
    setup.find_element_by_xpath("//div[contains(text(),'Python3')]").click()
    setup.close()
    sleep(3)

def test_second_case(setup):
    setup.get("https://www.google.co.in")
    setup.find_element_by_name("q").send_keys("selenium")
    setup.close()
    sleep(3)
