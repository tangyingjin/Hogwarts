import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction

'''利用高级定位方法，再次改造测试用例'''


class TestApp:
    def setup(self):
        caps = {}
        # capabilities设置
        # 平台，Which mobile OS platform to use（iOS, Android, or FirefoxOS）
        caps["platformName"] = "android"
        # The kind of mobile device or emulator to use（可以随意取）
        caps["deviceName"] = "Android Emulator"
        # Android Only
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # 是否在测试前后重置相关环境
        caps["noReset"] = True
        # 已启动的app不杀死
        # todo：不自动重启app参数设置，会报selenium.common.exceptions.SessionNotCreatedException: Message: A new session could not be created. (Original error: Requested a new session but one was in progress)
        # caps["autoLaunch"] = False
        caps["dontStopAppOnReset"] = True
        # 是否需要输⼊⾮英⽂
        # 之外的语⾔并在测试完成后重置输⼊法
        # caps["unicodeKeyBoard"] = True
        # caps["resetKeyBoard"] = True
        # caps["skipServerInstallation"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)

    def test_search(self):
        # 改造用例
        # el4 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
        # el4.click()
        self.driver.find_element(MobileBy.ID, 'tv_agree').click()
        # el5 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        # el5.click()
        self.driver.find_element(MobileBy.ID, 'tv_search').click()
        # el6 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        # el6.send_keys("alibaba")
        # el6.send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, 'search_input_text').send_keys('alibaba')

    def test_search_get_price(self):
        self.driver.find_element(MobileBy.ID, 'tv_search').click()
        self.driver.find_element(MobileBy.ID, 'search_input_text').send_keys('alibaba')
        self.driver.find_element(MobileBy.ID, 'name').click()
        assert float(self.driver.find_element(MobileBy.ID, 'current_price').text) > 200

    def test_search_get_price_from_hk(self):
        self.driver.find_element(MobileBy.ID, 'tv_search').click()
        self.driver.find_element(MobileBy.ID, 'search_input_text').send_keys('alibaba')
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@resource-id,'title_container')]//*[@text='股票']").click()
        # https://www.w3schools.com/xml/xpath_syntax.asp
        hk_current_price=(MobileBy.XPATH,'//*[@text="09988"]/../../..//*[contains(@resource-id,"current_price")]')
        assert float(self.driver.find_element(*hk_current_price).text) >200
        # ui断言
        print(self.driver.find_element(*hk_current_price).get_attribute('resource-id'))



    def test_device(self):
        # 后台运行
        self.driver.background_app(5)
        self.driver.lock(5)
        self.driver.unlock()


    def test_uiselector(self):
        scroll_to_element=(MobileBy.ANDROID_UIAUTOMATOR,'new UiScrollable('
                'new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView('
                    'new UiSelector().text("5小时前").instance(0));')
        self.driver.find_element(*scroll_to_element).click()
    # http://appium.io/docs/en/writing-running-appium/android/uiautomator-uiselector/index.html

    def test_scroll(self):
        # 长按/滑动等TouchAction的应用
        size=self.driver.get_window_size()
        print(size)
        TouchAction(self.driver).long_press(x=size["width"]*0.5,y=size["height"]*0.8).move_to(x=size["width"]*0.5,y=size["height"]*0.2).release().perform()




    def teardown(self):
        time.sleep(60)
        self.driver.quit()
