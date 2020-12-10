from selenium.webdriver.common.by import By

from pageobjectexceise.page.base_page import BasePage
from pageobjectexceise.page.contact_page import Contact


class Main(BasePage):

    def add_member(self):
        self._driver.find_element(By.LINK_TEXT, '添加成员').click()
        return Contact(self._driver)

    def import_contacts(self):
        self._driver.find_element(By.LINK_TEXT, '导入通讯录').click()

    def memberjoin(self):
        pass

    def createMessage(self):
        pass

    def customersanysis(self):
        pass

    def chart(self):
        pass
