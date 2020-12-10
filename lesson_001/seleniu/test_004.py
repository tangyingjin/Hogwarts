import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test004:
    @classmethod
    def setup(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.get('https://testerhome.com/')
        cls.driver.maximize_window()
        # 隐式等待是全局有效
        cls.driver.implicitly_wait(10)

    def wait(self, timeout, method):
        WebDriverWait(self.driver, timeout).until(method)

    def test004(self):
        self.driver.find_element(By.LINK_TEXT,'社团').click()
        self.driver.find_element(By.CSS_SELECTOR,'[data-name=霍格沃兹测试学院]').click()
        self.driver.find_element(By.CSS_SELECTOR,'.topic .title a').click()



    def test004_001(self):
        self.driver.find_element(By.LINK_TEXT,'社团').click()
        # self.driver.find_element(By.PARTIAL_LINK_TEXT,'霍格沃兹测试学院').click()
        '''若要使用PARTIAL_LINK_TEXT定位，则需要加显示等待'''
        element=(By.PARTIAL_LINK_TEXT,'霍格沃兹测试学院')
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(By.PARTIAL_LINK_TEXT,'霍格沃兹测试学院').click()
        self.driver.find_element(By.CSS_SELECTOR, '.topic:nth-child(1) .title a').click()

    def test004_002(self):
        self.driver.find_element(By.LINK_TEXT,'社团').click()
        element=(By.PARTIAL_LINK_TEXT,'霍格沃兹测试学院')
        # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(element))
        self.wait(10,expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()
        self.driver.find_element(By.CSS_SELECTOR,'.topic .title a').click()


    def test_hogwarts(self):
        self.driver.find_element(By.LINK_TEXT, '社团').click()
        # sleep(1)
        # todo: 显式等待
        # 尽量使用css的定位方法集，link有可能会导致解析元素的时候出现异常

        element = (By.PARTIAL_LINK_TEXT, '霍格沃兹测试学院')
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(element))
        # WebDriverWait(self.driver, 10).until(lambda x: self.driver.find_elements(element)>1)

        self.driver.find_element(*element).click()
        # 使用css比link更好用
        # self.driver.find_element(By.CSS_SELECTOR, '[data-name="霍格沃兹测试学院"]').click()
        # done：隐式等待
        self.driver.find_element(By.CSS_SELECTOR, '.topic:nth-child(1) .title a').click()

    @classmethod
    def teardown(cls):
        time.sleep(5)
        cls.driver.quit()