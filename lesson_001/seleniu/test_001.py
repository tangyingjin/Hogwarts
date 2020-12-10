import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestTesterhome:
    @classmethod
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://testerhome.com/')
        # todo:隐式等待（默认0.5s巡查下元素是否出现）
        self.driver.implicitly_wait(10)


    def test_001(self):

        self.driver.find_element(By.LINK_TEXT,'社团').click()
        # time.sleep(2)
        # todo:显示等待
        # 使用link_text比ss定位要早，因为link_text是发现元素就点击，此时元素还未真正地渲染出来。css是等整个页面加载完成后才会去定位元素
        # 尽量使用css的定位方法集，link有可能会导致解析元素的时候出现异常
        '''selenium.common.exceptions.StaleElementReferenceException:
         Message: stale element reference: element is not attached to the page document'''
        # self.driver.find_element(By.LINK_TEXT,'霍格沃兹测试学院').click()
        element=(By.PARTIAL_LINK_TEXT,'霍格沃兹测试学院')
        # WebDriverWait是个类，WebDriverWait（）实例化
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()
        # WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,'[data-name=霍格沃兹测试学院]')))
        # self.driver.find_element(By.CSS_SELECTOR,'[data-name=霍格沃兹测试学院]').click()

        # self.driver.find_element(By.XPATH,'//*[@id="main"]/div/div[1]/div/div[1]/div[1]/div[2]/div[1]/a').click()
        # 未加复数，找第一个
        # todo:隐式等待
        # self.driver.find_element(By.CSS_SELECTOR,'.topic .title a').click()
        self.driver.find_element(By.CSS_SELECTOR,'.topic:nth-child(1) .title a').click()

    @classmethod
    def teardown_class(self):
        time.sleep(5)
        self.driver.quit()