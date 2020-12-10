from selenium.webdriver.common.by import By

from lesson_001.pageobject.pages.basepages import BasePages


class SendMessage(BasePages):
    def sendmessage(self,app='',content='',group=''):
        locator=(By.LINK_TEXT,'选择需要发消息的应用')
        # self.find(locator).click()
        self._driver.execute_script("arguments[0].click();",self.find(locator))
        self.find(By.CSS_SELECTOR,'div[data-name*=%s]' %app).click()
        self.find(By.LINK_TEXT,'确定').click()

        locator=(By.LINK_TEXT,'选择发送范围')
        self._driver.execute_script("arguments[0].click();",self.find(locator))
        # self._driver.find_elements(By.CSS_SELECTOR,'.ww_searchResult_itemTxt')[-1].send_keys(group)
        # 为什么写成一行就报错
        element = self._driver.find_elements(By.CSS_SELECTOR, ".ww_searchInput_text")[-1]
        element.send_keys(group)
        self.find(By.CSS_SELECTOR, '#searchResult li').click()
        self.find(By.LINK_TEXT, '确认').click()

        self.find(By.CSS_SELECTOR,'textarea.js_send_msg_text').send_keys(content)
        locator=(By.LINK_TEXT, '发送')
        self._driver.execute_script("arguments[0].click();",self.find(locator))
        locator=(By.LINK_TEXT,'确定')
        self._driver.execute_script("arguments[0].click();",self.find(locator))


    def get_history(self):
            pass




