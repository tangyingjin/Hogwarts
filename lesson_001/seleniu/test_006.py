import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

'''frame切换，switch_to.frame根据元素或序号切换'''
'''多窗口切换，window_handles获取句柄，switch_to.window根据获取得句柄切换'''
'''执行javascript脚本'''

class Test006:
    @classmethod
    def setup(cls):
        browser=os.getenv('browser','').lower()
        if browser=='headless':
            cls.driver=webdriver.PhantomJS()
        elif browser=='firefox':
            cls.driver=webdriver.Firefox()
        else:
            # 使用headless模式
            options=webdriver.ChromeOptions()
            # options.add_argument('--headless')
            # options.add_argument('--disable-gpu')
            # options.add_argument('--window-size=1280,1696')

            # 使用已经存在的Chrome进程
            # 1.设置 Chrome 远程调试端口,windows右键点击 Chrome 的快捷方式图标，选择属性;在目标一栏，最后加上--remote-debugging-port=9222 注意要用空格隔开
            # 2.打开Chrome浏览器
            # 3.运行case，会在已有的浏览器中直接进行
            options.debugger_address='127.0.0.1:9222'
            cls.driver=webdriver.Chrome(options=options)

        cls.driver.implicitly_wait(6)

    def wait(self,time,method):
        WebDriverWait(self.driver,time).until(method)

    def test006(self):
        self.driver.get('https://testerhome.com/topics/21495')
        # self.driver.switch_to.frame(0)
        self.driver.switch_to.frame(self.driver.find_elements(By.TAG_NAME,'iframe')[0])
        pageSource=self.driver.page_source
        assert '抱歉！你访问的表单已停止收集数据' in pageSource

    def test006_001(self):
        self.driver.get('https://testerhome.com/topics/21805')
        # self.driver.set_window_size(1440,877)
        self.driver.find_element(By.LINK_TEXT,'第六届中国互联网测试开发大会').click()
        print(self.driver.window_handles)
        self.wait(10,lambda x:len(self.driver.window_handles) > 1 )
        self.driver.switch_to.window(self.driver.window_handles[1])
        element=(By.PARTIAL_LINK_TEXT,'演讲申请')
        self.driver.save_screenshot('3.png')
        self.wait(10,expected_conditions.presence_of_element_located(element))
        self.driver.find_element(*element).click()
        # print(self.driver.window_handles)
        # self.driver.switch_to.window(self.driver.window_handles[2])
        # self.driver.find_element(By.NAME,'username').send_keys('tangyingjin')
        # self.driver.find_element(By.CSS_SELECTOR,'.filePrew').click()
    #     todo：上传附件
    #     self.driver.find_element(By.CSS_SELECTOR,'.filePrew').send_keys(r'F:\12DD3E7E.png')

    def test006_002(self):
        self.driver.get('https://testerhome.com/')
        command=['return document.title',' return document.querySelector(".active").className','return JSON.stringify(performance.timing)']
        for code in command:
            js=self.driver.execute_script(code)
            print(js)



    @classmethod
    def teardown(cls):
        time.sleep(7)
        cls.driver.quit()