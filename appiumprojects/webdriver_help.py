from appium import webdriver
'''from .webdriver import WebDriver as Remote
from .webelement import WebElement'''

# from .webdriver import WebDriver as Remote
'''class WebDriver(
    AppiumSearchContext,
    ActionHelpers,
    Activities,
    Applications,
    Clipboard,
    Context,
    Common,
    DeviceTime,
    Display,
    ExecuteDriver,
    ExecuteMobileCommand,
    Gsm,
    HardwareActions,
    ImagesComparison,
    IME,
    Keyboard,
    Location,
    LogEvent,
    Network,
    Performance,
    Power,
    RemoteFS,
    ScreenRecord,
    Session,
    Settings,
    Sms,
    SystemBars
):

    def __init__(self, command_executor='http://127.0.0.1:4444/wd/hub',
                 desired_capabilities=None, browser_profile=None, proxy=None, keep_alive=True, direct_connection=False):'''
'''
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

from appium.webdriver.mobilecommand import MobileCommand as Command


class Activities(webdriver.Remote):
    def start_activity(self, app_package, app_activity, **opts):'''
# webdriver.Remote继承自selenium的remote webdriver
# appium的webdriver多继承了Activities等多种移动端的扩展实现
# appium driver <- Activities <- selenium remote webdriver(父类)