from .browser_action import *
from .test_data import *
from .locators import *

def launch_browser(url):
    driver.get(url)

def enter_text_to_search_box(value):
    input_text(driver, 'name', google_search_box, value)

def click_on_google_search_button():
    click_element(driver, 'name', google_search_button)


# This function will work with explicit wait
def enter_text_to_search_box_2(value):
    input_data(google_search_box_2, value)