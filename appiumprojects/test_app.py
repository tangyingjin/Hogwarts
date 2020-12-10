import time

from appium import webdriver

'''利用测试框架，改造成测试用例'''
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
        # caps["noReset"]=True
        # 是否需要输⼊⾮英⽂
        # 之外的语⾔并在测试完成后重置输⼊法
        caps["unicodeKeyBoard"] = True
        # caps["resetKeyBoard"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)

    def test_search(self):
        # el4 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
        # el4.click()
        el5 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        el5.click()
        el6 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el6.send_keys("alibaba")
        # todo:输入英文可以，输入中文失败,可能是unicodeKeyBoard参数不生效
        # el6.send_keys("阿里巴巴")

    def teardown(self):
        time.sleep(20)
        self.driver.quit()
