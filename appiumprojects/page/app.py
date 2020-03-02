from appium import webdriver

from appiumprojects.page.basepage import BasePage
from appiumprojects.page.main import Main


class App(BasePage):
    _appPackage = "com.xueqiu.android"
    _appActivity = ".view.WelcomeActivityAlias"
    def start(self):
        if self._driver is None:
            caps = {}
            # capabilities设置
            # 平台，Which mobile OS platform to use（iOS, Android, or FirefoxOS）
            caps["platformName"] = "android"
            # The kind of mobile device or emulator to use（可以随意取）
            caps["deviceName"] = "Android Emulator"
            # Android Only
            caps["appPackage"] = self._appPackage
            caps["appActivity"] = self._appActivity
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(20)
        else:
            print(self._driver)
            self._driver.start_activity(self._appPackage,self._appActivity)
        #     todo:self._appPackage访问类变量

        # return self当前实例自身，可继续调用当前类的其他方法（return self来实现链式调用）
        return self

    def restart(self):
        pass

    def stop(self):
        pass

    # 雪球app主界面
    def main(self) -> Main:
        # 返回值的类型是Main类型，类型提示 Type Hints
        # python2也提供了类型的支持，是IDE；并不是Python2自带的；从python3.6开始支持类型
        return Main(self._driver)
