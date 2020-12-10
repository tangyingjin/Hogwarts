'''使用android 6.0的模拟器

港美股开户
输入手机号与错误的验证码 1234
点击开户
切换回原生
点击关闭回到交易页'''
from appium import webdriver


class TestWebview:
    def setup(self):
        caps={}
        caps["platformName"] = "android"
        caps["deviceName"] = "Android Emulator"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"

        self.driver=webdriver