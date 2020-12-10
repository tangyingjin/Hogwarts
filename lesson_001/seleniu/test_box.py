import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestBox():
    def setup(self):
        # 加载chrome配置
        ChromeOptions=Options()
        ChromeOptions.add_experimental_option('debuggerAddress','127.0.0.1:9222')
        self.driver=webdriver.Chrome(options=ChromeOptions)
        self.driver.implicitly_wait(5)

    def test_box(self):
        self.driver.get('http://www.baidu.com')
        element=self.driver.find_element(By.LINK_TEXT,'设置')
        ActionChains(self.driver).move_to_element(element).perform()
        self.driver.find_element(By.LINK_TEXT,'搜索设置').click()
        time.sleep(2)
        self.driver.find_element(By.ID,'s1_2').click()
        if self.driver.find_element(By.ID,'s1_2').is_selected()==True:
            return


