from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from automation.test_data.env import wait_time
from selenium.webdriver.common.by import By



class BrowserAction:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, wait_time)
        #element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, "//input@id='id1"))

    # def input_text1(self, selector):
    #     if selector[0] == 'XPATH':
    #         self.driver.find_element_by_xpath(selector[1])
    #     elif selector[0] == 'ID':
    #         self.driver.find_element_by_id(selector[1])
    #     elif selector[0] == 'css':
    #         self.driver.find_element_by_css_selector(selector[1])

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
