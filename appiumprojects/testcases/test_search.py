import pytest

from appiumprojects.page.app import App


class TestSearch:
    def setup(self):
        self.main=App().start().main()

    def test_search(self):
        assert self.main.goto_search_page().search('alibaba').get_price('BABA') >200



    @pytest.mark.parametrize("key,stock_type,price",[
                             ("alibaba","BABA",200),
                              ("JD","JD",30)
    ])
    def test_search_data(self,key,stock_type,price):
        assert self.main.goto_search_page().search(key).get_price(stock_type) >price
#     todo:参数化跑用例失败
# self.main.goto_search_page().search(key).get_price(stock_type)返回的类型是float,与int类型可以进行正常比较的
# Pytest中装饰器@pytest.mark.parametrize('参数名',list)可以实现测试用例参数化;
# 第一个参数是字符串，多个参数中间用逗号隔开;第二个参数是list,多组数据用元祖类型;传三个或更多参数也是这样传。list的每个元素都是一个元组，元组里的每个元素和按参数顺序一一对应
#单参数单值@pytest.mark.parametrize("user",["18221124104"])
#单参数多值@pytest.mark.parametrize("user",["18221124104","18200000000","18200000001"])

