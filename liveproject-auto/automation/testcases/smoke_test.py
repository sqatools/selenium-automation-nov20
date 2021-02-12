from automation.test_data.env import *
from automation.test_data.variables import *
from time import sleep
from automation.test_data.variables import *

# def test_search_on_google(setup):
#     setup.launch_url(url)
#     setup.g_obj.search_data_on_google(google_search_data)
#     sleep(10)
#

def test_search_flight(setup):
    sleep(5)
    setup.f_obj.select_source_location(source_location)
    sleep(5)
    setup.f_obj.select_destination_location(destination_location)
    sleep(5)
    setup.f_obj.select_depart_date()
    setup.f_obj.select_return_date()
    sleep(5)
    setup.f_obj.select_number_of_travellers(adult=adults)
    sleep(5)
    setup.f_obj.click_on_search_button()
    sleep(10)
    setup.f_obj.select_maxprice_flight_for_depart()
    sleep(10)
    setup.f_obj.select_maxprice_flight_for_return()
    sleep(10)
    setup.f_obj.click_on_book_button()
    sleep(10)