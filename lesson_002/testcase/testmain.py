from lesson_002.pageobject.mainpage import MainPage


class TestMain:
    def test_add_user(self):
        # 初始化实例
        main=MainPage()
        # 链式调用
        main.add_user().add_user('cc')
        # 消息的断言
        assert 'a' in main.import_user().get_message()