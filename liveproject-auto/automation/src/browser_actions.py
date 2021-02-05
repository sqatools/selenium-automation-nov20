from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from automation.test_data.env import wait_time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class BrowserAction:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, wait_time)

    def input_text(self, selector, value):
        element = self.wait.until(EC.presence_of_element_located(selector))
        element.clear()
        element.send_keys(value)

    def click_element(self, selector):
        element = self.wait.until(EC.presence_of_element_located(selector))
        element.click()


    def get_list_of_elements(self, selector):
        elements = self.wait.until(EC.presence_of_all_elements_located(selector))
        return elements

    def get_element_text(self, selector):
        element = self.wait.until(EC.presence_of_element_located(selector))
        return element.text


    def select_value_from_dropdown(self, selector, value):
        element = self.wait.until(EC.presence_of_element_located(selector))
        sel_obj = Select(element)
        sel_obj.select_by_visible_text(value)

