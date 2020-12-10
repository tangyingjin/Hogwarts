from selenium import webdriver
from selenium.webdriver.common.by import By
from lesson_003.page.indexpage import IndexPage


class TestLogin:
    def setup(self):
        self.index = IndexPage()



    def test_login(self):
        self.index.goto_login()
        self.index.goto_register().registerpage('测试吧')

