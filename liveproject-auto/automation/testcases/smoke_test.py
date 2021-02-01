from automation.test_data.env import *
from automation.test_data.varaibles import *
from time import sleep

def test_search_on_google(setup):
    setup.launch_url(url)
    setup.g_obj.search_data_on_google(google_search_data)
    sleep(10)