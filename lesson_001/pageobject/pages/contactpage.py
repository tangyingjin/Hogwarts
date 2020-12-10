import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from lesson_001.pageobject.pages.basepages import BasePages


class Contact(BasePages):

        def add_member(self):
            self.find(By.ID, 'username') .send_keys('tangyingying')
            self.find(By.ID, 'memberAdd_acctid').send_keys('123')
            self.find(By.CSS_SELECTOR, '.ww_radio[value="2"]').click()
            # 定位企业微信的手机号,先点击，再定位下拉框
            self.find(By.CSS_SELECTOR, '.ww_telInput_zipCode_input').click()
            self.find(By.CSS_SELECTOR, 'li[data-value="86"]').click()
            self.find(By.ID, 'memberAdd_phone').send_keys('12345678901')
            self._driver.find_elements(By.CSS_SELECTOR, '.js_btn_save')[1].click()
            assert self.find(By.ID,'js_tips').text in '保存成功'


        def import_member(self,path):
            self.find(By.LINK_TEXT, '导入通讯录').click()
            self.find(By.ID,'js_upload_file_input').send_keys(path)
            # self.find(By.ID,'memberSearchInput').send_keys('财务部')
            # self.find(By.CSS_SELECTOR,'[tilte="练习测试账户/财务部"]').click()
            self.find(By.ID,'submit_csv').click()
            self.find(By.ID,'reloadContact').click()
