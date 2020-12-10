from selenium.webdriver.common.by import By

from lesson_002.pageobject.basepage import BasePage
from lesson_002.pageobject.register import Register


class Login(BasePage):
    _base_url='https://work.weixin.qq.com'
    def search_qrocode(self):
        pass

    def goto_register(self):
        self._driver.find_element(By.LINK_TEXT, '企业注册').click()
        return Register(self._driver)
