import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from lesson_001.pageobject.pages.basepages import BasePages


class ManagerTool(BasePages):
    def managertlool(self):
        self.find(By.LINK_TEXT,'管理工具').click()
        # 素材库如何定位
        # self.find(By.LINK_TEXT,'素材库').click()
        self.find(By.CSS_SELECTOR,'#js_manageTools_index > div > ul > li:nth-child(5) > a > div > div.manageTools_cnt_item_desc_title').click()
        self.find(By.CSS_SELECTOR,'.ww_icon_GrayPic').click()
        self.find(By.CSS_SELECTOR,'.ww_commonImg_AddMember').click()
        self.find(By.NAME,'uploadImageFile').send_keys(r'C:\Users\tangyingjin\PycharmProjects\lesson_001\pageobject\1581507855(1).jpg')
        # 如何校验图片上传成功,编辑和删除按钮
        loator=(By.CSS_SELECTOR,'.js_show_image')
        WebDriverWait(self._driver,150).until(expected_conditions.element_to_be_clickable(loator))
        self.find(By.CSS_SELECTOR,'js_next').click()