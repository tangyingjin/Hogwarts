from selenium.webdriver.common.by import By

from PageObject.page.basepages import BasePages
from PageObject.page.register_page import Register

class Login(BasePages):
    def goto_register(self):
        self._driver.find_element(By.LINK_TEXT,'企业注册').click()
        return Register(self._driver)

