'''企业微信未登陆首页'''
from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObject.page.index_page import Index


class TestIndex:
    def setup(self):
        self.index=Index()

    def test_register(self):
        self.index.goto_register().register("abc").GetErrorMessage()

    def teardown(self):
        self.index.close()