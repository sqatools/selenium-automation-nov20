from selenium.webdriver.common.by import By
from automation.test_data.variables import *

XPATH = By.XPATH
NAME = By.NAME
CSS = By.CSS_SELECTOR
ID = By.ID

SEARCH_BOX = (XPATH, "//input[@name='q']")
SEARCH_BUTTON =(XPATH, "(//input[@name='btnK'])[2]")
FLIGHT_OPTION = (XPATH, "//span[text()='Flights']")
SRC_FLIGHT_SEARCH =(ID, "gosuggest_inputSrc")
SRC_SEARCH_ELEMENTS = (XPATH, "//ul[@id='react-autosuggest-1']//li//*")
DEST_FLIGHT_SEARCH = (ID, "gosuggest_inputDest")
DEPART_BOOKING_DATE = (ID, f"fare_202102{depart_date}")
RETURN_BOOKING_DATE = (ID, f"fare_202102{return_date}")
RETURN_DATE_CALENDER = (ID, "returnCalendar")
PASSENGER_DETAILS = (ID, "pax_link_common")
ADULT_BOX = (ID, "adultPaxBox")
CHILD_BOX = (ID, "childPaxBox")
INFANT_BOX = (ID, "infantPaxBox")
TRAVEL_CLASS_DROPDOWN = (ID, "gi_class")

SEARCH_BUTTON = (ID, "gi_search_btn")

DEPART_FLIGHT_PRICES = (XPATH, "//div[@class='fltHpyOnwrdWrp']//span[@class='ico20']")
RETUNR_FLIGHT_PRICES = (XPATH, "//div[@class='fltHpyRtrnWrp']//span[@class='ico20']")
BOOK_BUTTON = (XPATH, "//input[@value='BOOK']")

####################
BUS_MENU_OPTION = (XPATH, "(//a[@href='/sbus/'])[1]")
BUS_FROM_LOCATION = (ID, "autosuggestBusSRPSrcHome")
# //span[text()='Mumbai, Maharashtra']

BUS_DEST_LOCATION = (ID, "autosuggestBusSRPDestHome")
BUS_TARVEL_DATE_CALENDER = (XPATH, "//input[@data-testid='openCheckinCalendar']")
BUS_TRAVEL_DATE = (XPATH, "//span[text()='19'")
BUS_SEARCH_BUTTON = (XPATH, "//button[@data-testid='searchBusBtn']")