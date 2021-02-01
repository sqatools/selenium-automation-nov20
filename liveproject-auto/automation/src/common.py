from .browser_actions import BrowserAction
from .locators import *
from .google_search import google_search

class common(BrowserAction):
    def __init__(self, driver):
        super().__init__(driver)
        self.g_obj = google_search(driver)

    def launch_url(self, url):
        self.driver.get(url)