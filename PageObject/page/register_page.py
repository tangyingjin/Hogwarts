from selenium.webdriver.common.by import By
from PageObject.page.basepages import BasePages


class Register(BasePages):
    def register(self,data):
        self._driver.find_element(By.ID,'corp_name').send_keys(data)
        self._driver.find_element(By.ID,'iagree').click()
        self._driver.find_element(By.ID,'submit_btn').click()
        # 返回当前页，返回self,才可以继续调用geterrormessage方法,是为了继续调用此类的其他方法
        return self

    def GetErrorMessage(self):
        result=[]
        for element in  self._driver.find_elements(By.CSS_SELECTOR,'.js_error_msg'):
            result.append(element.text)
        return result

