# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class TestApidemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "Android Emulator"
        caps["appPackage"] = "com.example.android.apis"
        caps["appActivity"] = ".ApiDemos"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)

    def test_toast(self):
        scroll_to_element=(MobileBy.ANDROID_UIAUTOMATOR,'new UiScrollable('
                'new UiSelector().scrollable(true).instance(0))'
                '.scrollIntoView('
                    'new UiSelector().text("Views").instance(0));')
        self.driver.find_element(*scroll_to_element).click()
        scroll_to_element1=(MobileBy.ANDROID_UIAUTOMATOR,'new UiScrollable('
                'new UiSelector().scrollable(true).instance(0))'
                 '.scrollIntoView('
                    'new UiSelector().text("Popup Menu").instance(0));')
        self.driver.find_element(*scroll_to_element1).click()
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID,"Make a Popup!").click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="Edit"]').click()
        element=(By.XPATH,"//*[@class='android.widget.Toast']")
        assert 'Edit' in self.driver.find_element(*element).text

    def teardown(self):
        self.driver.quit()
