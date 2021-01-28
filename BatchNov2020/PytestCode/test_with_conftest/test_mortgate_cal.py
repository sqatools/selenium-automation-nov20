from time import sleep
from selenium.webdriver.support.ui import Select
from .locators import *


def test_home_price(setup, teardown):
    setup.find_element_by_id(HOME_PRICE_ID).clear()
    setup.find_element_by_id(HOME_PRICE_ID).send_keys(4000)
    sleep(5)

def test_downpayment(setup, teardown):
    setup.find_element_by_id(DOWN_PAYMENT_ID).clear()
    setup.find_element_by_id(DOWN_PAYMENT_ID).send_keys(30)
    sleep(5)

def test_loanayment(setup, teardown):
    setup.find_element_by_id(LOAN_TERMS_ID).clear()
    setup.find_element_by_id(LOAN_TERMS_ID).send_keys(20)
    sleep(5)

def test_interestrate(setup, teardown):
    setup.find_element_by_id(INTEREST_RATE_ID).clear()
    setup.find_element_by_id(INTEREST_RATE_ID).send_keys(9)
    sleep(5)

def test_startdate(setup, teardown):
    select_obj = Select(setup.find_element_by_id(START_DATE_DROPDOWN_ID))
    select_obj.select_by_visible_text('Aug')
    setup.find_element_by_id(DATE_YEAR_ID).clear()
    setup.find_element_by_id(DATE_YEAR_ID).send_keys(2022)
    sleep(5)