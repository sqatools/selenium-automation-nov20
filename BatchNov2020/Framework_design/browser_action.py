from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .test_data import driver_path

driver = webdriver.Chrome(executable_path=driver_path)
driver.maximize_window()

# Implicit wait
driver.implicitly_wait(10)

# Explicit wait
wait = WebDriverWait(driver, 20)


def click_element(driver, type, selector):
    if type == 'xpath':
        driver.find_element_by_xpath(selector).click()
    elif type == 'id':
        driver.find_element_by_id(selector).click()
    elif type == 'css':
        driver.find_element_by_css_selector(selector).click()
    elif type == 'name':
        driver.find_element_by_name(selector).click()

# This is work with implicit wait
def input_text(driver, type, selector, value):
    if type == 'xpath':
        driver.find_element_by_xpath(selector).send_keys(value)
    elif type == 'id':
        driver.find_element_by_id(selector).send_keys(value)
    elif type == 'css':
        driver.find_element_by_css_selector(selector).send_keys(value)
    elif type == 'name':
        driver.find_element_by_name(selector).send_keys(value)

# This will work with explicit wait
def input_data(selector, value):
    wait.until(EC.presence_of_element_located(selector)).send_keys(value)