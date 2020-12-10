import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestTotal:
    def setup(self):
        ChromeOptions=Options()
        ChromeOptions.add_experimental_option('debuggerAddress','127.0.0.1:9222')
        self.driver=webdriver.Chrome()


    def test_alert(self):
        '''去掉页面动态窗(alert窗)'''
        self.driver.get('https://www.runoob.com/try/try.php?filename=tryjs_alert')
        self.driver.switch_to.frame('iframeResult')
        self.driver.find_element(By.CSS_SELECTOR,'[value="显示警告框"]').click()
        time.sleep(2)
        self.driver.switch_to.alert.accept()


    def test_001(self):
        '''定位百度首页上更多产品里面的全部产品'''
        self.driver.get('http://www.baidu.com')
        self.driver.maximize_window()
        menu=self.driver.find_element(By.NAME,'tj_briicon')
        ActionChains(self.driver).move_to_element(menu).perform()
        # 谷歌浏览器处理滚动条
        # js="var q=document.body.scrollTop=10000"
        # 火狐浏览器处理滚动条
        # js="var q=document.documentElementscrollTop=10000"
        # self.driver.execute_script(js)

        # 元素聚焦，也是可以解决的
        target=self.driver.find_element(By.NAME,'tj_more')
        self.driver.execute_script("arguments[0].scrollIntoView();",target)
        # 定位到更多产品
        self.driver.find_element(By.NAME,'tj_more').click()

       # 获取百度联想词
    def test_002(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element(By.ID,'kw').send_keys('博客')
        elements=self.driver.find_elements(By.CLASS_NAME,'bdsug-overflow')
        # for i in elements:
        #     print(i.get_attribute('data-key'))
        if len(elements)>1:
            elements[1].click()

