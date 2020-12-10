import time
from selenium import webdriver
from selenium.webdriver.common.by import By

'''未加任何等待，报：selenium.common.exceptions.ElementClickInterceptedException:
 Message: element click intercepted: Element <a title="...'''
class Test002:
    @classmethod
    def setup(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.get('https://testerhome.com/')

    def test002(self):
        self.driver.find_element(By.LINK_TEXT,"社团").click()
        self.driver.find_element(By.LINK_TEXT,"霍格沃兹测试学院").click()
        self.driver.find_element(By.CSS_SELECTOR,'.topic .title a').click()

    @classmethod
    def teardown(cls):
        time.sleep(5)
        cls.driver.quit()

