from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.sqatools.in/2020/08/dropdown.html")
sleep(3)
select_obj = Select(driver.find_element_by_id('cars'))

select_obj.select_by_index(2)

sleep(3)

select_obj.select_by_visible_text("Land Rover")

sleep(3)

select_obj.select_by_value("jaguar")

sleep(3)

driver.close()



