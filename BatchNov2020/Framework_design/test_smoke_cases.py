from .features import *
from .test_data import *
from time import  sleep

# This will work with implicit wait
# def test_search_data_on_google(setup):
#     enter_text_to_search_box(search_content)
#     sleep(5)
#     click_on_google_search_button()
#     sleep(5)

def test_search_data_on_google_2(setup):
    enter_text_to_search_box_2(search_content)
    sleep(5)
    click_on_google_search_button()
    sleep(5)
