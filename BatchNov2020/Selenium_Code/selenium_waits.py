from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


#1. Imlicit wait : IT applies on all the element unconditionally
#2. Explicit Wait : It will apply on specific element and poll for particular
#3. static wait : It is hard sleep to perform any action on web page.

driver = webdriver.Chrome(executable_path="E:\\python-selenium-code-Nov20\\selenium-automation-nov20\\liveproject-auto\\automation\\drivers\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)   # It will apply on all the element with out any condition

wait = WebDriverWait(driver, 20) # It will apply on specific element to perform operation

driver.get("https://www.google.co.in")


driver.find_element_by_name('q').send_keys("Selenium")

element = wait.until(EC.presence_of_element_located((By.NAME,'btnK')))

element.click()

sleep(5)
driver.close()