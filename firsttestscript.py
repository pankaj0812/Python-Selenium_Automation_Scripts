from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\Projects\\Python_Automation_Testing\\chromedriver_win32\\chromedriver.exe")
driver.get("http://www.google.com")
print("First Test Script is completed")