from time import sleep

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
# selenium.webdriver.remote.webdriver.WebDriver 这个类其实是所有其他Webdriver的父类，
# 例如Chrome Webdriver，Firefox Webdriver都是继承自这个类。这个类中实现了每个Webdriver间相通的方法。


class BasePage:
    def __init__(self, driver:WebDriver=None):
        if driver is None:
            # index页面会使用这个
            self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(3)
            self._driver.get(self._base_url)
            # self._driver.get('https://work.weixin.qq.com')
        else:
            # Login与Register等页面需要用这个方法
            self._driver = driver

    def close(self):
        sleep(20)
        self._driver.quit()

