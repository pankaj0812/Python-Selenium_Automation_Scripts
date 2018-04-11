from selenium import webdriver

driver = webdriver.Firefox(executable_path="D:\\Projects\\Python_Automation_Testing\\geckodriver-v0.20.1-win64\\geckodriver.exe")
driver.get("http://www.twitter.com")
print("navigated to twitter")