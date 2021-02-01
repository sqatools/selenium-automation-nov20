class BrowserAction:
    def __init__(self, driver):
        self.driver = driver

    def input_text(self, selector, value):
        self.driver.find_element_by_xpath(selector).send_keys(value)

    def click_element(self, selector):
        self.driver.find_element_by_xpath(selector)