from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\Projects\\Python_Automation_Testing\\chromedriver_win32\\chromedriver.exe")
driver.get("http://www.gmail.com")
driver.find_element_by_name("identifier").send_keys("abc.defpksingh@gmail.com")
driver.find_element_by_xpath("//*[@id='identifierNext']/content/span").click()

driver.implicitly_wait(5)
driver.find_element_by_name("password").send_keys("iwanttodie")
driver.implicitly_wait(4)
driver.find_element_by_xpath("//*[@id='passwordNext']/content/span").click()
driver.implicitly_wait(4)

driver.find_element_by_xpath("//*[@id='gb']/div[1]/div[1]/div[2]/div[5]/div[1]/a/span").click()
driver.implicitly_wait(4)
driver.find_element_by_xpath("//*[@id='gb_71']").click()

print("Gmail is tested")


