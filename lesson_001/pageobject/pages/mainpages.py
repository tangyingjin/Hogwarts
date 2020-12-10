from selenium.webdriver.common.by import By

from lesson_001.pageobject.pages.basepages import BasePages
from lesson_001.pageobject.pages.contactpage import Contact
from lesson_001.pageobject.pages.sendmessagepage import SendMessage


class Main(BasePages):
    _base_url ='https://work.weixin.qq.com/wework_admin/frame#index'

    def add_member(self):
        locator=(By.LINK_TEXT, '添加成员')
        # self.find(locator).click()
        self._driver.execute_script("arguments[0].click();",self.find(locator))
        return Contact(reuse=True)

    def import_member(self):
        pass
    def download(self):
        pass

    def send_messger(self):
        self.find(By.LINK_TEXT, '消息群发').click()
        return SendMessage(reuse=True)

