from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    base_url = ''

    def __init__(self, driver: WebDriver = None, reuse=False):
        if driver is None:
            if reuse:
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
        else:
            return self.driver.find_element(by, locator)
