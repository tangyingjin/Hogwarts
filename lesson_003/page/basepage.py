from selenium import webdriver


class BasePage:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.get('https://work.weixin.qq.com/')
        