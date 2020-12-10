from selenium import webdriver
from selenium.webdriver.common.by import By
from lesson_001.pageobject.pages.contactpage import Contact
from lesson_001.pageobject.pages.mainpages import Main
from lesson_001.pageobject.pages.managertoolpage import ManagerTool
from lesson_001.pageobject.pages.sendmessagepage import SendMessage


class TestIndex():
    contact=Contact(reuse=True)
    main = Main(reuse=True)

    def test_import_member(self):
        self.contact.import_member(r"C:\Users\tangyingjin\PycharmProjects\lesson_001\pageobject\通讯录批量导入模板.xlsx")

    def test_managertool(self):
        ManagerTool(reuse=True).managertlool()

    def test_sendmessger(self):
        message=self.main.send_messger()
        message.sendmessage(app='测试开发',content='测试数据',group='汤瑛瑾')
        assert  'content' in message.get_history()