from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\Projects\\Python_Automation_Testing\\chromedriver_win32\\chromedriver.exe")
driver.get("http://www.google.com")
driver.refresh()
driver.forward()
driver.get("http://www.bing.com")
driver.refresh()
driver.back()
driver.get("http://www.bing.com")
print("All urls are navigated successfully")
driver.quit()