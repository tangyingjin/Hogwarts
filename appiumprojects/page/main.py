from appium.webdriver.common.mobileby import MobileBy

from appiumprojects.page.basepage import BasePage
from appiumprojects.page.profile import Profile
from appiumprojects.page.search import Search


class Main(BasePage):
    # _drvier: WebDriver

    # def __init__(self, driver):
    #     self._driver = driver

    # 搜索框
    def goto_search_page(self):
        self.find(MobileBy.ID, 'tv_search').click()
        return Search(self._driver)

    # 跳转行情页
    def goto_stocks(self):
        pass

    # 跳转交易页
    def goto_trade(self):
        pass

    # 跳转我的
    def goto_profile(self):
        self.find(MobileBy.XPATH, '//*[@text="我的"]').click()
        return Profile(self._driver)
