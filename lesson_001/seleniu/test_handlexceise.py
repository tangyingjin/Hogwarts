from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestHandle():
    def wait(self,timeout,method):
        WebDriverWait(self.driver,timeout).until(method)
    def setup(self):
        ChromeOptions=Options()
        ChromeOptions.add_experimental_option('debuggerAddress','127.0.0.1:9222')
        self.driver=webdriver.Chrome(options=ChromeOptions)

    # 多窗口切换
    def test_handle(self):
        self.driver.get('http://www.bj.ganji.com')
        self.driver.find_element(By.LINK_TEXT,'全职').click()
        # 获取所有窗口的句柄
        windows=self.driver.window_handles
        self.wait(10,lambda x:len(self.driver.window_handles)>1)
        # 获取当前窗口的句柄
        # self.driver.switch_to.window(self.driver.current_window_handle)
        self.driver.switch_to.window(windows[1])
        self.driver.find_element(By.ID,'search_keyword').send_keys('测试工程师')
        # 切换首页窗口句柄
        self.driver.switch_to.window(windows[0])
        print(self.driver.title)

    # iframe切换
    def test_handle01(self):
        self.driver.get('https://mail.163.com')
        self.driver.find_element(By.ID,'switchAccountLogin').click()
        # 切换iframe
        self.driver.switch_to.frame(self.driver.find_elements(By.TAG_NAME,'iframe')[0])
        self.driver.find_element(By.NAME,'email').send_keys('12345678901')
        self.driver.find_element(By.NAME,'password').send_keys('123456789')
        self.driver.find_element(By.ID,'dologin').click()
        # 释放iframe,重新回到主界面
        self.driver.switch_to.default_content()

