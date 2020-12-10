from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObject.page.basepage import PageBase
from PageObject.page.basepages import BasePages
from  PageObject.page.register_page import Register
from PageObject.page.login_page import Login
'''企业微信首页的立即注册'''

class Index(BasePages):
    '''可以设置每一个页面的url'''
    _base_url='https://work.weixin.qq.com'

    def goto_register(self):
        self._driver.find_element(By.LINK_TEXT,'立即注册').click()
        return Register(self._driver)

    def goto_login(self):
        self._driver.find_element(By.LINK_TEXT,'企业登录').click()
        return Login(self._driver)

