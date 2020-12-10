#测试企业注册
from selenium import webdriver
from lesson_002.pageobject.index import Index



class TestIndex:
    def setup(self):
        self.index=Index()

        # 初始化driver
        # self.driver = webdriver.Chrome()
        # # 隐式等待
        # self.driver.implicitly_wait(3)
        #
        # self.driver.get('https://work.weixin.qq.com/')
    def test_register(self):

        # 初始化driver
        # self.driver=webdriver.Chrome()
        # # 隐式等待
        # self.driver.implicitly_wait(3)
        # self.driver.get('https://work.weixin.qq.com/')
        # self.driver.find_element(By.LINK_TEXT, '立即注册').click()

        # self.driver.find_element(By.ID,'corp_name').send_keys('测试')
        # self.driver.find_element(By.ID,'submit_btn').click()

        self.index.goto_register().register('测试')


    def test_login(self):
        self.index.goto_login().goto_register().register('测吧')


    def teardown(self):
        self.index.close()