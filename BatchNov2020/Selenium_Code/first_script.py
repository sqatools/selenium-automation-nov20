from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:\\drivers\\chromedriver_win32\\chromedriver.exe')

driver.get("https://www.sqatools.in/p/home.html")

driver.find_element_by_xpath('//a[text()="Python 3 Tutorial"]').click()

time.sleep(5)

driver.close()





