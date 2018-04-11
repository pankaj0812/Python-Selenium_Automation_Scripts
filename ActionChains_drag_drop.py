from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="D:\\Projects\\Python_Automation_Testing\\chromedriver_win32\\chromedriver.exe")
driver.get("http://jqueryui.com/droppable/")
driver.implicitly_wait(3)
driver.switch_to.frame(0)

source = driver.find_element_by_id("draggable")
target = driver.find_element_by_id("droppable")
ActionChains(driver).drag_and_drop(source, target).perform()
print("drag and drop completed")