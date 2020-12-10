import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebView:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "Android Emulator"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # caps["noReset"] = True
        # caps["autoLaunch"] = False
        # caps["chromedriverExecutableDir"]="/Users/seveniruby/projects/chromedriver/all"
        # caps["chromedriverExecutable"] = "/Users/seveniruby/projects/chromedriver/all/chromedriver_2.20"
        caps['avd'] ="my_android_devices"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)

    def test_webview_native(self):
        # webview用源生的定位，但是有很多副作用
        self.driver.find_element(MobileBy.XPATH, '//*[@text="交易" and contains(@resource-id,"tab")]').click()
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'A股开户').click()
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, '港交所上市互联网证券试点券商').click()
        # open=(MobileBy.ACCESSIBILITY_ID,'港交所上市互联网证券试点券商')
        # WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(open))
        # todo:老师的雪球步骤和我的不一致，视频再看下
        time.sleep(2)
        phone = (MobileBy.XPATH, '//android.widget.EditText')
        for element in self.driver.find_elements(*phone):
            try:
                element.send_keys('15678901110')
            except Exception as e:
                print(element.get_attribute('content-desc'))
                print(element.get_attribute('class'))
                print(element.get_attribute('resource-id'))
                print(e)
        # todo:老师sendkeys不生效原因，我操作是可以输入的，但是手机号和验证码都输入了同一个了，需要处理下
        # 对于webview控件使用webview的定位方法

    def test_webview_context(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="交易" and contains(@resource-id,"tab")]').click()
        # 首次做测试的时候，用于分析当前的窗口
        # for i in range(5):
        #     print(self.driver.contexts)
        #     # appium处理app与web页面的转换:switch_to_context
        #     time.sleep(0.5)
        # print(self.driver.page_source)
        WebDriverWait(self.driver, 10).until(lambda x: len(self.driver.contexts) > 1)
        self.driver.switch_to.context(self.driver.contexts[-1])
        # print(self.driver.page_source)
        # A股开户
        print(self.driver.window_handles)
        self.driver.find_element(By.CSS_SELECTOR, '.trade_home_info_3aI').click()

        # 首次做测试的时候，用于分析当前的窗口
        for i in range(5):
            print(self.driver.window_handles)
            time.sleep(0.5)
        WebDriverWait(self.driver, 10).until(lambda x: len(self.driver.window_handles) > 3)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # 平安证券开户
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, '港交所上市互联网证券试点券商').click()
        # 开户，输入手机号
        phone = (By.ID, 'phone-number')
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(phone))
        self.driver.find_element(*phone).send_keys('15678901110')

    def test_webview_teachercode(self):
        self.driver.find_element(By.XPATH, "//*[@text='交易' and contains(@resource-id, 'tab')]").click()

        # 首次做测试的时候，用于分析当前的上下文
        # for i in range(5):
        #     print(self.driver.contexts)
        #     sleep(0.5)
        # print(self.driver.page_source)

        # 坑1：webview上下文出现大概有3s的延迟, android 6.0默认支持，其他的需要打开webview调试开关
        # adb shell cat /proc/net/unix | grep  webview
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.contexts) > 1)
        # 坑2：chromedriver的版本与chrome版本必须对应(selenium.common.exceptions.WebDriverException: Message: An unknown server-side error occurred while processing the command. Original error: No Chromedriver found that can automate Chrome '44.0.2403'. You could also try to enable automated chromedrivers download server feature.
        # See https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/web/chromedriver.md for more details)
        # 坑3：chromedriver可能会存在无法对应chrome版本的情况，需要使用caps的mapping file或者直接chromedriverExecutable
        # /Users/seveniruby/projects/chromedriver/all/chromedriver_2.20 --url-base=wd/hub --port=8000 --adb-port=5037 --verbose

        self.driver.switch_to.context(self.driver.contexts[-1])
        # print(self.driver.page_source)
        # print(self.driver.window_handles)

        # 使用chrome inspect分析界面控件，需要代理、需要chrome62及以前的版本都可以
        # Proxying [POST /wd/hub/session/b2fe71d1-3dff-45df-bc2c-52e9195d5b98/element] to [POST http://127.0.0.1:8000/wd/hub/session/790fc7cf4c186545679b24ce5bbd9699/element] with body: {"using":"css selector","value":".trade_home_info_3aI"}
        self.driver.find_element(By.CSS_SELECTOR, ".trade_home_info_3aI").click()

        # 首次做测试的时候，用于分析当前的窗口
        # for i in range(5):
        #     print(self.driver.window_handles)
        #     sleep(0.5)

        # 坑4：可能会出现多窗口，所以要注意切换
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.window_handles) > 3)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        phone = (By.ID, 'phone-number')

        # html定位的常见问题，元素可以找到的时候，不代表可以交互，需要用显式等待
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located(phone))
        self.driver.find_element(*phone).send_keys("15600534760")
        
        
    def test_avd(self):
        self.driver.find_element(By.XPATH, "//*[@text='交易' and contains(@resource-id, 'tab')]").click()

