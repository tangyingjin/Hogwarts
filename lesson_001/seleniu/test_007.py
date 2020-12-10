'''selenium多浏览器处理'''
'''PhantomJS 是一个基于Webkit的“无界面”(headless)浏览器，它会把网站加载到内存并执行页面上的 JavaScript，
因为不会展示图形界面，所以运行起来比完整的浏览器要高效。
os.getenv(key, default=None) 获取环境变量，如果存在则返回环境变量键的值，如果不存在返回None（或者设置的默认值）
os.getenvb(key, default=None) 同上，结果为字节
terminal运行browser=chrome失败，(venv) C:\Users\tangyingjin\PycharmProjects>set browser=chrome&& pytest -s C:\Users\tangyingjin\PycharmProjects\lesson_001\seleniu\test_007.py
'''
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

class Test007:
    @classmethod
    def setup(cls):
        browser=os.getenv('browser').lower()
        print(browser)
        if browser=='headless':
            # 调用环境变量指定的PhantomJS浏览器创建浏览器对象
            cls.driver=webdriver.PhantomJS()
        elif browser=='chrome':
            cls.driver=webdriver.Chrome()
        else:

            cls.driver=webdriver.Firefox()


        cls.driver.get('https://testerhome.com/topics/21495')
        cls.driver.implicitly_wait(5)

    def test007(self):
        self.driver.switch_to.frame(self.driver.find_elements(By.TAG_NAME,'iframe')[0])
        pageSource=self.driver.page_source
        assert '抱歉！你访问的表单已停止收集数据' in pageSource

    def teardown(self):
        self.driver.quit()

