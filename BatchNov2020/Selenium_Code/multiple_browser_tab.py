from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.sqatools.in/p/manual-testing.html")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element_by_xpath("//a[contains(text(),'What is Software Testing')]").click()
driver.switch_to.window(driver.window_handles[1])

element = driver.find_element_by_xpath("//h3[contains(text(),'Software Testing')]")
print("Element :", element.text)
assert element != None
sleep(5)
driver.close()

"""
driver.switch_to.window(driver.window_handles[0])

sleep(5)
driver.find_element_by_xpath("//a[contains(text(),' What is Manual Testing')]").click()
driver.switch_to.window(driver.window_handles[1])
sleep(5)
driver.close()
driver.switch_to.window(driver.window_handles[0])
sleep(5)
driver.close()

"""

