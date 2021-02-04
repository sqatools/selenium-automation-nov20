from selenium.webdriver.common.by import By

# This will work with implicit wait
google_search_box = "q"
google_search_button = "btnK"


NAME = By.NAME
XPATH = By.XPATH
ID = By.ID
CSS = By.CSS_SELECTOR

# This will ork with explicit wait
google_search_box_2 = (NAME, "q")

