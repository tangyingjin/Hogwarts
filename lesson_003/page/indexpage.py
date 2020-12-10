from selenium.webdriver.common.by import By

from lesson_003.page.basepage import BasePage
from lesson_003.page.registerpage import RegisterPage


class IndexPage(BasePage):

    def goto_register(self):
        self.driver.find_element(By.LINK_TEXT, '企业注册').click()
        return RegisterPage(self.driver)

    def goto_login(self):
        self.driver.find_element(By.LINK_TEXT, '企业登录').click()
