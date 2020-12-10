import time

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePages:
    def __init__(self,driver:WebDriver=None):
        if driver is None:
            self._driver=webdriver.Chrome()
            self._driver.implicitly_wait(5)
            self._driver.get(self._base_url)
        else:
            self._driver=driver

    def close(self):
        time.sleep(10)
        self._driver.quit()