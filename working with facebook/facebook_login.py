from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\Projects\\Python_Automation_Testing\\chromedriver_win32\\chromedriver.exe")
driver.get("http://www.facebook.com")
driver.find_element_by_name("email").send_keys("******@gmail.com")
driver.find_element_by_name("pass").send_keys("*******")
driver.find_element_by_id("loginbutton").click()

driver.implicitly_wait(3)