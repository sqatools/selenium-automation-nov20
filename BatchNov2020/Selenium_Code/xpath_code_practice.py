from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:\\drivers\\chromedriver_win32\\chromedriver.exe')

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()


#driver.find_element_by_xpath("//input[@name='fromcity']").send_keys("Mumbai")
time.sleep(5)
#driver.find_element_by_xpath("//input[@type='checkbox']").click()

# CONTAINS METHODS
#driver.find_element_by_xpath("//input[contains(@name,'billing_post')]").send_keys('3343454')

'''
# Get all the elements the contains billing in their name attribute
# and perform operation on that

element_list = driver.find_elements_by_xpath("//input[contains(@name,'billing')]")
data_list = ['23424235', 'test@gmail.com', 'Mumbai', 'Khar', 'Mumbai', 'Maharastra', '1233443']
temp = 0
for element in element_list:
    element.send_keys(data_list[temp])
    temp = temp+1

'''

'''
# AND & or OPERATION
driver.find_element_by_xpath("//input[contains(@id,'bill') and @name='billname']").send_keys("234235")
'''

# Text Method
#driver.find_element_by_xpath("//label[text()=' Add more passengers:']").click()


# Following Method
driver.find_element_by_xpath("//label[text()='Choose option']//following::input[@id='deliverymethod_2']").click()



'''
# Ancestor 
elem_xpath = "//span[@itemprop='price']//span[contains(text(), '1,200')]//ancestor::li//input[@type='radio']"
driver.find_element_by_xpath(elem_xpath).click()
'''


time.sleep(5)
driver.close()