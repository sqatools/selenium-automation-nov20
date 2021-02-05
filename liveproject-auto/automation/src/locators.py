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

