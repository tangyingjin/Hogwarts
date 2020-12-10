'''css定位符

document.querySelectorAll('.active')
$('.active')
$x('//*[@data-name="霍格沃兹测试学院"]')
'''
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

'''
css定位百度输入框：
1.$('input#kw')
2.$('[name="wd"]')
3.$('[autocomplete="off"]')
'''
'''
selenium遇到得坑：
1.UI自动化时，解决selenium中无法点击Element：ElementClickInterceptedException
在跑自动化时，页面上有2个下拉框，两个下拉框无论屏蔽哪一段都会成功，但是同时放开跑时会报错，百度给的解释是上面的下拉框元素覆盖了下面下拉框的元素定位，才会导致报错
百度得解决方案：
1.element = driver.find_element_by_css('div[class*="loadingWhiteBox"]')
driver.execute_script("arguments[0].click();", element)
2.element = driver.find_element_by_css('div[class*="loadingWhiteBox"]')
webdriver.ActionChains(driver).move_to_element(element ).click(element ).perform()

2.selenium+webdriver错误selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable (Session info: chrome=75.0.3770.142)

'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestCss():
    def setup(self):
        ChromeOptions = Options()
        ChromeOptions.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
        self.driver = webdriver.Chrome(options=ChromeOptions)
        self.driver.implicitly_wait(5)

    def test_css(self):
        self.driver.get('https://testerhome.com/topics/21854')
        self.driver.find_element(By.CSS_SELECTOR, '.media div:nth-child(3)  a:nth-child(1) div:nth-child(1)').click()
        # 截屏
        # self.driver.get_screenshot_as_file('1.png')
        # self.driver.save_screenshot('2.png')
        # close关闭当前窗口
        # self.driver.close()
        # quit结束所有进程
        # self.driver.quit()

    def test_css_01(self):
        self.driver.get('http://www.baidu.com')
        # 鼠标悬浮到设置按钮上
        menu = self.driver.find_element(By.LINK_TEXT, '设置')
        ActionChains(self.driver).move_to_element(menu).perform()

        # 点击搜索设置
        element2 = (By.PARTIAL_LINK_TEXT, '搜索设置')
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(element2))
        self.driver.find_element(*element2).click()
        # 必须要加等待时间，不然下拉选择框点击不到，解决方案第一种，time.sleep(2)生效
        time.sleep(2)
        # 2.使用循环点击不生效，不知道为什么
        # WebDriverWait(self.driver,555).until(self.wait_element)

        # select下拉选择框，导入Select模块
        # s=self.driver.find_element(By.ID,'nr')
        # Select(s).select_by_index(0)
        # select下拉选择框，使用直接定位
        self.driver.find_element(By.ID, 'nr').find_element(By.CSS_SELECTOR, 'select#nr option:nth-child(3)').click()

        # 解决element click intercepted，保存设置
        element = self.driver.find_elements(By.LINK_TEXT, '保存设置')
        self.driver.execute_script("arguments[0].click();", *element)

        # 弹出框，获取alert弹框
        var = self.driver.switch_to.alert
        print(var.text)
        var.accept()

    # 练习操作元素（键盘和鼠标事件）
    def test_css02(self):
        self.driver.get('http://www.baidu.com')
        # 鼠标事件，send_keys,clear,submit
        self.driver.find_element(By.ID, 'kw').send_keys('python教程')
        # self.driver.find_element(By.ID,'kw').clear()
        # self.driver.find_element(By.ID,'kw').submit()
        # 键盘事件,Keys.ENTER回车，Keys.CONTROL,'a'
        self.driver.find_element(By.ID, 'kw').send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, 'kw').send_keys(Keys.CONTROL, 'a')

    def wait_element(self, x):
        size = len(self.driver.find_elements(By.XPATH, '//*[@id="nr"]/option'))
        if size < 3:
            self.driver.find_element(By.ID, 'nr').find_element(By.CSS_SELECTOR, 'select#nr option:nth-child(1)').click()
        return size
