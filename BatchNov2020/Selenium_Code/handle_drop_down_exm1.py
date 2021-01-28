from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
sleep(3)

depart_id = 'departon'
month_drop_down_css = 'select.ui-datepicker-month'
#year_drop_down_css = 'select.ui-datepicker-year'
year_dropdown_xpath = "//select[@class='ui-datepicker-year']"
'''
driver.find_element_by_id(depart_id).click()
######### month ############
sleep(2)
select_mon = Select(driver.find_element_by_css_selector(month_drop_down_css))
sleep(2)
select_mon.select_by_visible_text('Aug')
select_year = Select(driver.find_element_by_css_selector(year_drop_down_css))
sleep(2)

########## Year ###############
select_year.select_by_visible_text('2019')
sleep(2)
driver.find_element_by_xpath("//a[text()='20']").click()
sleep(5)
'''

def select_value_dropdown(type, element, value):

    # select = Select(driver.find_element_by_css_selector(element))
    # select.select_by_visible_text(value)
    if type=='id':
        select = Select(driver.find_element_by_id(element))
        select.select_by_visible_text(value)
    elif type == 'xpath':
        select = Select(driver.find_element_by_xpath(element))
        select.select_by_visible_text(value)
    elif type == 'name':
        select = Select(driver.find_element_by_name(element))
        select.select_by_visible_text(value)
    elif type == 'css':
        select = Select(driver.find_element_by_css_selector(element))
        select.select_by_visible_text(value)


driver.find_element_by_id(depart_id).click()
select_value_dropdown('css', month_drop_down_css, 'Aug')
sleep(3)
select_value_dropdown('xpath', year_dropdown_xpath, '2019')
sleep(3)
driver.find_element_by_xpath("//a[text()='20']").click()

sleep(5)

driver.close()



