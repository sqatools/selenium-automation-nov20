from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

id = driver.find_element_by_id
xpath = driver.find_element_by_xpath
css = driver.find_element_by_css_selector


# Country Drop down
drop_down_id = "select2-billing_country-container"
search_field_xpath = "//input[@class='select2-search__field']"
search_data = 'India'
#//li[text()='India']
list_xpath = f"//li[text()='{search_data}']"

# Passesnger Drop down
checkbxo_id = 'addmorepax'
pass_dropdown_id = 'select2-addpaxno-container'
list_value_xpath = "//li[text()='add 2 more passengers']"


#Country dropdown
id(drop_down_id).click()
sleep(2)
xpath(search_field_xpath).send_keys(search_data)
sleep(2)
xpath(list_xpath).click()

sleep(5)

# Passenger drop down
id(checkbxo_id).click()
sleep(2)
id(pass_dropdown_id).click()
sleep(2)
xpath(list_value_xpath).click()
sleep(2)

driver.close()



