from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\Projects\\Python_Automation_Testing\\chromedriver_win32\\chromedriver.exe")
driver.get("http://www.google.com")
print("First Test Script is completed")
driver.get("http://www.twitter.com")
print("navigated to Twitter")
driver.get("http://www.gmail.com")
print("navigated to Gmail")