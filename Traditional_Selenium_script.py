import unittest
from selenium import webdriver

class TraditionalWay(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="D:\\Projects\\Python_Automation_Testing\\chromedriver_win32\\chromedriver.exe")

    def test_google_search_page(self):
        driver = self.driver
        driver.get("http://www.google.com")


if __name__ == '__main__':
    unittest.main()
