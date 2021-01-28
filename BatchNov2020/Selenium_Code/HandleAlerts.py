from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.sqatools.in/2020/08/alerts.html")

"""
# Handle Alert Box
driver.find_element_by_id("btnShowMsg").click()
alertobj = driver.switch_to.alert
sleep(1)
print(alertobj.text)
alertobj.accept()
"""

# Handle Confirm Box
"""
driver.find_element_by_id("button").click()

alertobj1 = driver.switch_to.alert
print(alertobj1.text)
sleep(1)
alertobj1.accept()

alert_msg = driver.find_element_by_id("demo").text
print(alert_msg)
assert alert_msg == "You pressed OK!"


sleep(2)
# Cancel box
driver.find_element_by_id("button").click()

alertobj11 = driver.switch_to.alert
print(alertobj1.text)
sleep(1)
alertobj11.dismiss()

alert_msg1 = driver.find_element_by_id("demo").text
print(alert_msg1)
assert alert_msg1 == "You pressed Cancel!"
"""



# Prompt Box
driver.find_element_by_id("promptbtn").click()

prompt_alert = driver.switch_to.alert

print(prompt_alert.text)
prompt_alert.send_keys("SQA Tools")
sleep(1)
prompt_alert.accept()

prompt_msg = driver.find_element_by_id("prompt").text

print(prompt_msg)
assert prompt_msg == "Hello SQA Tools! How are you today?"

driver.close()
