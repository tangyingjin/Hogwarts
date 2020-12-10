from selenium.webdriver.common.by import By

# 注册页的pageObject
from lesson_002.pageobject.basepage import BasePage


class Register(BasePage):
    # def __init__(self,driver):
    #     self.driver=driver

    def register(self,corpname):
        self._driver.find_element(By.ID, 'corp_name').send_keys(corpname)
        self._driver.find_element(By.ID, 'submit_btn').click()
