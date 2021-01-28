from selenium import webdriver
from time import sleep


browser = "edge"
driver = None

if browser == "chrome":
    driver = webdriver.Chrome()
elif browser == "firefox":
    driver = webdriver.Firefox(executable_path="E:\\driver\\geckodriver.exe")
elif  browser == 'edge':
    driver = webdriver.Edge(executable_path="E:\\driver\\msedgedriver.exe")


driver.get("https://www.sqatools.in/p/manual-testing.html")
driver.maximize_window()
driver.implicitly_wait(10)


def handle_multiple(driver):
    driver.find_element_by_xpath("//a[contains(text(),'What is Software Testing')]").click()
    driver.switch_to.window(driver.window_handles[1])
    element = driver.find_element_by_xpath("//h3[contains(text(),'Software Testing')]")
    print("Element :", element.text)
    assert element != None
    sleep(5)
    driver.close()

handle_multiple(driver)

driver.quit()