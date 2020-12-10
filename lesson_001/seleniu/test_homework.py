import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

'''作业1:进入testerhome，访问MTSC2020置顶帖，点击目录，点击议题征集范围
   作业2：企业微信自动添加成员，需要复用已经登录的chrome，需要debugger address。
   作业3：多浏览器并行测试，server服务器用于分发，node用于运行'''
class Test005:
    @classmethod
    def setup(cls):
        chromeOptions=Options()
        chromeOptions.add_experimental_option('debuggerAddress','127.0.0.1:9222')
        cls.driver=webdriver.Chrome(options=chromeOptions)
        # options=webdriver.ChromeOptions()
        # options.debugger_address='127.0.0.1:9222'
        # cls.driver=webdriver.Chrome(options=options)
        cls.driver.implicitly_wait(1)

    def test_005(self):
        self.driver.get('https://testerhome.com/')
        element=By.PARTIAL_LINK_TEXT,'MTSC2020 中国互联网测试开发大会议题征集'
        self.wait(10,expected_conditions.element_to_be_clickable(element))
        # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()
        self.driver.find_element(By.CSS_SELECTOR,'.panel-default div:nth-child(2) button.btn-default').click()
        self.driver.find_element(By.CSS_SELECTOR,'.list-container ul:nth-child(1) li:nth-child(2) a.toc-item-link').click()


    def test_005_001(self):
        # 点击通讯录
        self.driver.find_element(By.ID,'menu_contacts').click()
        # 点击添加成员
        self.driver.find_elements(By.CSS_SELECTOR,'.js_add_member')[2].click()

        # 显示等待也失败，response = {'status': 404, 'value': '{"value":{"error":"no such element","message":"no such element: Unable to locate element}
        # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,'.js_has_member div:nth-child(1) .js_add_member')))
        # 显示等待失败，1.使用sleep
        # time.sleep(2)
        # 显示等待失败，2.循环点击元素
        # while True:
        #       time.sleep(0.5)
        #     self.wait_element()
        WebDriverWait(self.driver,10).until(self.wait_element)
        # self.driver.find_element(By.CSS_SELECTOR,'.js_has_member div:nth-child(1) .js_add_member').click()
        self.driver.find_element(By.ID,'username').send_keys('tangtang')
        self.driver.find_element(By.ID,'memberAdd_acctid').send_keys('abc')
        self.driver.find_element(By.ID,'memberAdd_phone').send_keys('15268888888')
        self.driver.find_element(By.CSS_SELECTOR,'.js_btn_save').click()
    #     断言成员是否添加成功
    #     self.add_success()
        assert  len(self.driver.find_elements(By.CSS_SELECTOR,'[title="tangtang"]')) >=1

    def wait(self,timeout,method):
        WebDriverWait(self.driver,timeout).until(method)

    def wait_element(self,x):
        size=len(self.driver.find_elements(By.ID,'username'))
        if size<1:
            self.driver.find_element(By.CSS_SELECTOR, '.js_has_member div:nth-child(1) .js_add_member').click()
        return size


    def add_success(self):
        size=len(self.driver.find_elements(By.CSS_SELECTOR,'[title="tangtang"]'))
        if size >=1:
            print("添加成员成功")
        else:
            print("添加成员失败")
    def teardown(self):
        time.sleep(5)
        self.driver.quit()