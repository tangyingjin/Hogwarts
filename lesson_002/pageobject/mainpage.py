from lesson_002.pageobject.contactpage import Contact

# 返回的是其他页的po
class MainPage:
    #首页的pageobject
    def download(self):
        pass

    def import_user(self):
        # 返回当前页
        return self

    def goto_app(self):
        pass

    def goto_company(self):
        pass

    def get_message(self):
        # 返回消息是个列表
        return ['a','n']

    def add_user(self):
        # 返回实例化对象，对象包含add_user方法
        return Contact()
