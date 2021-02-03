from .browser_actions import BrowserAction
from .locators import *
from .google_search import google_search
from .flight_booking import flight

class common(BrowserAction):
    def __init__(self, driver):
        super().__init__(driver)
        self.g_obj = google_search(driver)
        self.f_obj = flight(driver)

    def launch_url(self, url):
        self.driver.get(url)