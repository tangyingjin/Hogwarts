from lesson_002.pageobject.contactpage import Contact

# case中只需要写做什么，内部实现的逻辑与细节都封装在PO里
class TestContact:
    def test_add_user(self):
        # 初始化实例
        contact=Contact()
        # 调用实例方法
        contact.add_user('测试')
