from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from workweixin.pageobject.page.basepage import BasePage

'''企业微信添加用户'''


class Contact(BasePage):

    def add_member(self, name='', acctid='', mobile=''):
        # 姓名
        username_locator=(By.ID, 'username')
        self.find_element(username_locator).send_keys(name)
        # 账号
        acctid_locator=(By.NAME, 'acctid')
        self.find_element(acctid_locator).send_keys(acctid)
        # 性别
        gender_locator=(By.CSS_SELECTOR,'.ww_radio[value="2"]')
        self.find_element(gender_locator).click()
        # 手机号码
        mobile_locator=(By.NAME, 'mobile')
        self.find_element(By.CSS_SELECTOR, '.ww_telInput_zipCode_input').click()
        self.find_element(By.CSS_SELECTOR, 'li[data-value="86"]').click()
        self.find_element(mobile_locator).send_keys(mobile)
        # 部门
        party_locator=(By.CSS_SELECTOR, '.js_show_party_selector')
        self.find_element(party_locator).click()
        # 设置滚动条
        js = "var q=document.body.scrollTop=0"
        self.driver.execute_script(js)
        # 选择成员所在部门
        e = self.driver.find_elements(By.CSS_SELECTOR, '.ww_searchInput_text')[-1].send_keys("财务")
        self.find_element(By.CSS_SELECTOR, '#searchResult li').click()
        self.find_element(By.LINK_TEXT, '确认').click()
        self.find_element(By.LINK_TEXT, '保存').click()
        return self

    def get_member(self):
        get_member_locator=(By.CSS_SELECTOR, '#member_list tr:nth-child(3) td:nth-child(2)')
        return self.find_element(get_member_locator).get_attribute('title')

    def update_member(self):
        menu = self.driver.find_element(By.CSS_SELECTOR, 'td[title="张三"]')
        ActionChains(self.driver).move_to_element(menu).perform()
        self.driver.find_elements(By.CSS_SELECTOR, '.js_dropdown_menuBtn')[-1].click()
        self.driver.find_element(By.LINK_TEXT, '编辑').click()
        self.driver.find_element(By.NAME, 'mobile').clear()
        self.driver.find_element(By.NAME, 'mobile').send_keys('12345678902')
        self.driver.find_element(By.LINK_TEXT, '保存').click()
        return self
