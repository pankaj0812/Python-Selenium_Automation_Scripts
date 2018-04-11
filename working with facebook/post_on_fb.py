from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.expected_conditions import alert_is_present

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")


driver = webdriver.Chrome(executable_path="D:\\Projects\\Python_Automation_Testing\\chromedriver_win32\\chromedriver.exe", chrome_options=chrome_options)
driver.get("http://www.facebook.com")
driver.find_element_by_name("email").send_keys("*******@gmail.com")
driver.find_element_by_name("pass").send_keys("******")
driver.find_element_by_id("loginbutton").click()

driver.implicitly_wait(5)

driver.find_element_by_name("xhpc_message").send_keys("Hello world.")
#driver.implicitly_wait(3)
driver.find_element_by_xpath("//button[@data-testid='react-composer-post-button']").click()

print("Sent keys successfully")