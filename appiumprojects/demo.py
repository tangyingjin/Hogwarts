# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
# coding=utf-8
'''利用appium desktop录制的脚本，不能称为case'''
from appium import webdriver
'''利用appium desktop录制的脚本，不能称为case'''



caps = {}
caps["platformName"] = "android"

caps["deviceName"] = "Android Emulator"
# |`deviceName`|使用的手机类型或模拟器类型|`iPhone Simulator`, `iPad Simulator`, `iPhone Retina 4-inch`, `Android Emulator`, `Galaxy S4`, 等。
# 在 iOS 上，这个关键字的值必须是使用 `instruments -s devices` 得到的可使用的设备名称之一。在 Android 上，这个关键字目前不起作用。|
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] =".view.WelcomeActivityAlias"
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)
el4 = driver.find_element_by_id("com.xueqiu.android:id/tv_agree")
el4.click()
el5 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el5.click()
el6 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el6.send_keys("alibaba")

driver.quit()
