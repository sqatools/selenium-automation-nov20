from selenium import webdriver
import time

#driver = webdriver.Chrome(executable_path='C:\\drivers\\chromedriver_win32\\chromedriver.exe')

driver = webdriver.Chrome(executable_path='C:\\drivers\\chromedriver_win32\\chromedriver.exe')

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

# By ID
#driver.find_element_by_id('travname').send_keys("SQA")

# By Name
#driver.find_element_by_name("travname").send_keys("Selenium")

# By Css Selector
#driver.find_element_by_css_selector("input[name='travname']").send_keys("CSS Selector")
#driver.find_element_by_css_selector("#travname").send_keys("CSS Selector")
#driver.find_element_by_css_selector("input#travname").send_keys("CSS Selector")
#driver.find_element_by_css_selector("div>p#order_comments_field>textarea").send_keys("We are in text area field")
#driver.find_element_by_css_selector("textarea[name='order_comments']").send_keys("We are in text area field")

label_text = driver.find_element_by_css_selector("p[id='order_comments_field']>label").text
print(label_text)
assert  label_text == 'Order Notes'

time.sleep(5)

driver.close()



