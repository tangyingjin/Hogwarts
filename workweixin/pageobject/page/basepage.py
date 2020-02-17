from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    base_url = ''

    def __init__(self, driver: WebDriver = None, reuse1=False):
        # reuse参数是自定义的
        if driver is None:
            if reuse1:
                ChromeOptions = Options()
                ChromeOptions.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
                self.driver = webdriver.Chrome(options=ChromeOptions)
            else:
                # 重新打开一个页面
                self.driver = webdriver.Chrome()
        else:
            self.driver = driver
        self.driver.implicitly_wait(5)

        # self.driver.get(base_url)
        # 不加self.base_url,只是一个没有定义的变量base_url
        if self.base_url != '':
            # 实例变量
            self.driver.get(self.base_url)
            # 类变量
            # self.driver.get(BasePage.base_url)

    def find_element(self, by, locator=''):
        if isinstance(by, tuple):
            return self.driver.find_element(*by)
        # selenium自带的find_element方法里传入的参数是两个,如果我们传入了元组,则必须解析
        else:
            return self.driver.find_element(by, locator)
