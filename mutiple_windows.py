from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\Projects\\Python_Automation_Testing\\chromedriver_win32\\chromedriver.exe")
driver.get("http://www.google.com")
driver.execute_script("window.open('http://www.amazon.in','new window')")
print("Amazon is opened in new window")

driver.implicitly_wait(5)
driver.switch_to.window(driver.window_handles[0])
driver.get("http://www.bing.com")
print("bing is opened in first window")

driver.switch_to.window(driver.window_handles[1])
driver.get("http://www.ask.com")
print("ask.com is opened in first window")

driver.execute_script("window.open('http://pankaj0812.github.io','new window')")
print("Portfolio successfully loaded")
driver.switch_to.window(driver.window_handles[1])