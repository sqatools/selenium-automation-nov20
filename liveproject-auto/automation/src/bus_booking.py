from automation.src.browser_actions import BrowserAction
from automation.src.locators import *
from time import sleep

class Bus(BrowserAction):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate_bus_booking_page(self):
        self.click_element(BUS_MENU_OPTION)

    def select_source_location(self,  src_location):
        self.input_text(BUS_FROM_LOCATION, src_location)
        sleep(2)
        element = self.driver.find_element_by_xpath(f"//span[text()='{src_location}']")
        element.click()

    def select_destination_location(self, dest_location):
        self.input_text(BUS_DEST_LOCATION, dest_location)
        sleep(2)
        element = self.driver.find_element_by_xpath(f"//span[text()='{dest_location}']")
        element.click()

    def select_date(self, date):
        self.click_element(BUS_TARVEL_DATE_CALENDER)
        sleep(2)
        element = self.driver.find_element_by_xpath(f"//span[text()='{date}']")
        element.click()

    def click_bus_search_button(self):
        self.click_element(BUS_SEARCH_BUTTON)

    def select_bus_to_travel(self, bus_name):
        locator = f"//p[text()='{bus_name}']//ancestor::div[contains(@class, 'Srpcardstyles')][4]//span[text()='SHOW BUSES']"
        self.click_element((XPATH, locator))
        select_seat = f"//p[text()='{bus_name}']//ancestor::div[contains(@class, 'SrpActiveCardstyles')]//span[text()='SELECT SEAT']"
        self.click_element((XPATH, select_seat))
