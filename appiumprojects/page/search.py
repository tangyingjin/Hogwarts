from appium.webdriver.common.mobileby import MobileBy

from appiumprojects.page.basepage import BasePage


class Search(BasePage):
    # def __init__(self, driver):
    #     self._driver = driver
    # todo:多平台、多版本、多个可能定位符
    _name_locator = (MobileBy.ID, 'name')

    def search(self, key: str):
        self.find(MobileBy.ID, "search_input_text").send_keys(key)
        self.find(self._name_locator).click()
        return self

    def get_price(self, key: str) -> float:
        # key:str输入的参数类型是str类型;
        # ->float:返回值类型是float
        return float(self.find(MobileBy.ID, 'current_price').text)
