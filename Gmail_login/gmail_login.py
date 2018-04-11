from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\Projects\\Python_Automation_Testing\\chromedriver_win32\\chromedriver.exe")
driver.get("http://www.gmail.com")
driver.find_element_by_name("identifier").send_keys("******@gmail.com")
driver.find_element_by_xpath("//*[@id='identifierNext']/content/span").click()

driver.implicitly_wait(5)
driver.find_element_by_name("password").send_keys("*******")
driver.find_element_by_xpath("//*[@id='passwordNext']/content/span").click()