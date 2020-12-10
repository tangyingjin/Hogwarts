from selenium import webdriver
from selenium.webdriver.common.by import By

from lesson_002.pageobject.basepage import BasePage
from lesson_002.pageobject.login import Login
from lesson_002.pageobject.register import Register


# 首页的PageObject
class Index(BasePage):
    # def __init__(self,driver=None):
    #     if driver==None:
    #         self.driver = webdriver.Chrome()
    #         # 隐式等待
    #         self.driver.implicitly_wait(3)
    #         self.driver.get('https://work.weixin.qq.com/')
    #     else:
    #         self.driver=driver
    _base_url = 'https://work.weixin.qq.com/'

    def goto_register(self):
        self._driver.find_element(By.LINK_TEXT, '立即注册').click()
        return Register(self._driver)

    def goto_login(self):
        self._driver.find_element(By.LINK_TEXT, '企业登录').click()
        return Login(self._driver)
# self.driver实例变量
