from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self,driver:WebDriver=None):
        if driver is None:
            self._ChromeOptions=Options()
            self._ChromeOptions.add_experimental_option("debuggerAddress",'127.0.0.1:9222')
            self._driver=webdriver.Chrome(options=self._ChromeOptions)
        else:
            self._driver=driver
        self._driver.implicitly_wait(5)
    def find_element(self):
        self._driver.find_element(By.ID,'q')