from appium.webdriver.common.mobileby import MobileBy

from appiumprojects.page.basepage import BasePage


class Profile(BasePage):
    def login_by_password(self, account, password):
        self.find(MobileBy.XPATH, '//*[@text="账户密码登录"]').click()
        self.find(MobileBy.ID, 'login_account').send_keys(account)
        self.find(MobileBy.ID, 'login_password').send_keys(password)
        self.find(MobileBy.ID, 'button_next').click()
        msg = self.find(MobileBy.ID, 'md_content').text
        self.find(MobileBy.ID, 'md_buttonDefaultPositive').click()
        return msg
