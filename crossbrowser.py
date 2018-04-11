from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
DesiredCapabilities = {}
DesiredCapabilities['platform'] = 'Windows'
DesiredCapabilities['browserName'] = 'Firefox'
DesiredCapabilities['browserName'] = 'GoogleChrome'

driver = webdriver.Chrome(executable_path="D:\\Projects\\Python_Automation_Testing\\chromedriver_win32\\chromedriver.exe")
driver.get("http://www.twitter.com")
print("twitter opened in Chrome")

driver = webdriver.Firefox(executable_path="D:\\Projects\\Python_Automation_Testing\\geckodriver-v0.20.1-win64\\geckodriver.exe")
driver.get("http://www.twitter.com")
print("twitter opened in Firefox")
