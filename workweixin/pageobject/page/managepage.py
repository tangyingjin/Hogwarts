from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from workweixin.pageobject.page.basepage import BasePage


class Manage(BasePage):
    base_url = 'https://work.weixin.qq.com/wework_admin/frame#manageTools'

    def load_picture(self):
        # 点击素材库
        material_locator = (By.CSS_SELECTOR, '[href="#material/text"]')
        # 点击图片
        goto_image_locator = (By.CSS_SELECTOR, '[href="#material/image"]')
        # 点击添加图片
        upload_file_locator = (By.CSS_SELECTOR, '.js_upload_file_selector')
        # 点击上传图片
        upload_input_loctor = (By.CSS_SELECTOR, '#js_upload_input')
        # 完成
        submit_locator=(By.CSS_SELECTOR, '.js_next')

        self.find_element(material_locator).click()
        self.find_element(goto_image_locator).click()
        self.find_element(upload_file_locator).click()
        self.find_element(upload_input_loctor).send_keys(r'C:\Users\tangyingjin\PycharmProjects\lesson_001\pageobject\1581507855(1).jpg')
        self.find_element(submit_locator).click()
        return self

    def get_picture(self):
        first_picture_locator=(By.CSS_SELECTOR,'.material_picCard_cnt_pic')
        return self.find_element(first_picture_locator).get_attribute('style')
        # editor_elment=(By.CSS_SELECTOR,'.js_enter_modify')
        # ActionChains(self.driver).move_to_element(editor_elment).perform()
