from selenium.webdriver.common.by import By


class Contact:
    # 设置私有变量，将控件实现的细节封装，内部细节不暴露
    # 断言加载测试用例里，不要加在PO里
    _add_user_button=(By.CSS,'XXX')

    def add_user(self, data):
        # self.driver.find_element("添加成员").click()
        # 成功的返回列表页
        return self 

    def add_user_error(self,data):
        # 添加成员信息错误返回的是详情页
        # return AddRemeberPage()
        pass

    def search(self):
        pass

    def import_user(self):
        pass

    def export_user(self):
        pass

    def set_department(self, data):
        pass

    def delete(self):
        pass

    def invite(self):
        pass
