from selenium.webdriver.common.by import By

from workweixin.pageobject.page.basepage import BasePage
from workweixin.pageobject.page.contactpage import Contact


class Main(BasePage):
    base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    # main类继承父类BasePage类，重新定义了base_url,则会覆盖父类的base_url

    def goto_member(self):
        # js定位
        element = self.find_element(By.LINK_TEXT, '添加成员')
        self.driver.execute_script("arguments[0].click();", element)
        # 显示等待
        # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(element))
        # self.driver.find_element(*element).click()
        return Contact(reuse1=True)
