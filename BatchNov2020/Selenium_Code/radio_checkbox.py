from selenium import  webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
URL = "https://www.dummyticket.com/dummy-ticket-for-visa-application/"
driver.get(URL)

# Select Radio Button
print(driver.find_element_by_id('sex_1').is_selected())

driver.find_element_by_id('sex_1').click()

print(driver.find_element_by_id('sex_1').is_selected())

# Select Box
driver.find_element_by_id('addmorepax').click()
driver.find_element_by_id('addmorepax').is_selected()
sleep(5)
driver.close()