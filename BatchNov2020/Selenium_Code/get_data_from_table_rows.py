from selenium import  webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

URL = 'http://dtemaharashtra.gov.in/StaticPages/frmInstituteList.aspx?RegionID=6&RegionName=Pune'

driver.get(URL)

id = driver.find_element_by_id
xpath = driver.find_element_by_xpath
css = driver.find_element_by_css_selector

college_list = driver.find_elements_by_xpath("//table[@class='DataGrid']//tr//td[3]")

num = 0
# for collect in college_list:
#     print(num, ":", collect.text)
#     num = num + 1

college_ids = driver.find_elements_by_xpath("//table[@class='DataGrid']//tr//td[2]/a[2]")
temp = 0
user_input = input("Please enter college ID :")

for id in college_ids:
    #print(id.text)
    if user_input == id.text:
        print(college_list[temp].text)
        break
    temp = temp + 1


