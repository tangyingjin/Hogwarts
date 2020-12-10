import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test003:
    @classmethod
    def setup(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.get('https://testerhome.com/')
        cls.driver.implicitly_wait(10)

    def test_003(self):
        self.driver.find_element(By.LINK_TEXT,'社团').click()
        self.driver.find_element(By.LINK_TEXT,'霍格沃兹测试学院').click()
        self.driver.find_element(By.CSS_SELECTOR,'.topic .title a').click()

    @classmethod
    def teardown(cls):
        cls.driver.quit()