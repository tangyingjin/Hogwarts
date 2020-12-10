from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePages:
    _base_url = ""
    _driver = None

    def __init__(self, driver: WebDriver = None, reuse=False):
        if driver is None:
            if reuse:
                options = webdriver.ChromeOptions()
                # 使用已经存在的chrome进程
                #  /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
                options.debugger_address = "127.0.0.1:9222"
                self._driver = webdriver.Chrome(options=options)
            else:
                # index页面会使用这个
                self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(3)
        else:
            # Login与Register等页面需要用这个方法
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)

    def find1(self, locator):
        return self._driver.find_element(*locator)
    #     可以使用self.find((By.LINK_TEXT, '添加成员')).click(),必须使用(())

    def find2(self,by,locator):
        return self._driver.find_element(by,locator)
    # 使用self.find(By.LINK_TEXT,'添加成员').click()

    def find(self,by,locator=''):
        if isinstance(by,tuple):
            return self._driver.find_element(*by)
        else:
            return self._driver.find_element(by,locator)


    def close(self):
        self._driver.quit()